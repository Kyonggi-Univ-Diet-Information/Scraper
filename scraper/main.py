import logging
import datetime
import subprocess
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

    process = CrawlerProcess(settings)
    process.crawl(DormSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
    result = subprocess.run(['python', 'upload.py'], capture_output=True, text=True)
    print(result.stdout)