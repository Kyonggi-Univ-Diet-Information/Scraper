from scrapy.crawler import CrawlerProcess
from scraper.spiders.dorm import DormSpider

def run_spider():
    process = CrawlerProcess()
    process.crawl(DormSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
