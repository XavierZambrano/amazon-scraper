import os
import json
from betamax import Betamax
from betamax.fixtures.unittest import BetamaxTestCase
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse

from amazon.spiders.product import ProductSpider


with Betamax.configure() as config:
    cassette_library_dir = 'test/fixtures/cassettes'
    os.makedirs(cassette_library_dir, exist_ok=True)
    config.cassette_library_dir = cassette_library_dir


class TestProductSpider(BetamaxTestCase):
    def setUp(self):
        super().setUp()

        process = CrawlerProcess(install_root_handler=False)
        process.crawl(ProductSpider)
        self.spider = list(process.crawlers)[0].spider

    def test_parse_asin(self):
        mock_response = self.get_mock_response('https://www.amazon.com/War-Peace-Penguin-Clothbound-Classics/dp/0241265541/')
        expected_result = '0241265541'

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['asin'], expected_result)

    def test_parse_title(self):
        mock_response = self.get_mock_response('https://www.amazon.com/War-Peace-Penguin-Clothbound-Classics/dp/0241265541/')
        expected_result = 'War and Peace (Penguin Clothbound Classics)'

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['title'], expected_result)

    def test_parse_price(self):
        mock_response = self.get_mock_response('https://www.amazon.com/War-Peace-Penguin-Clothbound-Classics/dp/0241265541/')
        expected_result = {
            'currency': 'USD',
            'value': 16.59
        }

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['price'], expected_result)

    def get_mock_response(self, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en', 'User-Agent': 'Scrapy/2.11.2 (+https://scrapy.org)',
            'Accept-Encoding': 'gzip, deflate'
        }
        response = self.session.get(url, headers=headers)
        if response.ok is False:
            raise ValueError(f'Request to {url} failed with status code {response.status_code}')
        scrapy_response = HtmlResponse(body=response.content, url=url)

        return scrapy_response
