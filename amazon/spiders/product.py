import scrapy


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://amazon.com"]

    def parse(self, response):
        pass
