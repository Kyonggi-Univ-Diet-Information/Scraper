import scrapy
from datetime import datetime
from scraper.items import ScraperItem

class DormSpider(scrapy.Spider):
    name = "dorm"
    allowed_domains = ["dorm.kyonggi.ac.kr"]

    def start_requests(self):
        today = datetime.now()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")

        url = f"https://dorm.kyonggi.ac.kr:446/Khostel/mall_main.php?viewform=B0001_foodboard_list&gyear={year}&gmonth={month}&gday={day}"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        decoded_body = response.body.decode('euc-kr')

        for row in response.css("table.boxstyle02 tbody tr"):
            date = row.css("th a::text").get() or row.css("th::text").get(default="").strip()
            meals = row.css("td")
            
            breakfast = ""
            lunch = ""
            dinner = ""

            if len(meals) > 0:
                breakfast = "&".join([item.strip() for item in meals[0].css("::text").getall() if item.strip()])
            if len(meals) > 1:
                lunch = "&".join([item.strip() for item in meals[1].css("::text").getall() if item.strip()])
            if len(meals) > 2:
                dinner = "&".join([item.strip() for item in meals[2].css("::text").getall() if item.strip()])

            yield {
                "date": date,
                "breakfast": breakfast if breakfast else "미운영",
                "lunch": lunch if lunch else "미운영",
                "dinner": dinner if dinner else "미운영",
            }
