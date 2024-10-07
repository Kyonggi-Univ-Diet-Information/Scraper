import logging
import datetime
from scrapy.crawler import CrawlerProcess
from scraper.spiders.dorm import DormSpider
from scrapy.utils.project import get_project_settings


def run_spider():
    settings = get_project_settings()

    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f'logs/scrapy_log_{current_time}.txt'

    logging.basicConfig(
        filename=log_filename,
        format='%(asctime)s [%(levelname)s] %(message)s',
        level=logging.DEBUG
    )

    process = CrawlerProcess()
    process.crawl(DormSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
