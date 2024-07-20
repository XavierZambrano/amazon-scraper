import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/Little-Black-Classics-Box-Penguin/dp/0141398876/"]

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
