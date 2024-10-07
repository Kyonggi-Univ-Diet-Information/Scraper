import scrapy


class DormSpider(scrapy.Spider):
    name = "dorm"
    allowed_domains = ["dorm.kyonggi.ac.kr"]
    start_urls = ["https://dorm.kyonggi.ac.kr"]

    def parse(self, response):
        pass
