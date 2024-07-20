import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["amazon.com"]

    def __init__(self, urls, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls.split(',')

    def parse(self, response):
        title = response.xpath('//h1[@id="title"]//text()[normalize-space()]').get()
        price_raw = response.xpath('//div[@class="cardRoot bucket"]/@data-price-totals').get()
        price_raw = json.loads(price_raw)
        price = price_raw['1']

        yield {
            'id': response.xpath('//input[@name="items[0.base][asin]"]/@value').get(),
            'title': title,
            'price': price
        }
