import scrapy
from datetime import datetime

class DormSpider(scrapy.Spider):
    name = "dorm"
    allowed_domains = ["dorm.kyonggi.ac.kr"]

    def start_requests(self):
            # 현재 날짜를 가져옵니다.
            today = datetime.now()
            year = today.strftime("%Y")
            month = today.strftime("%m")
            day = today.strftime("%d")

            # 동적으로 URL을 생성합니다.
            url = f"https://dorm.kyonggi.ac.kr:446/Khostel/mall_main.php?viewform=B0001_foodboard_list&gyear={year}&gmonth={month}&gday={day}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        decoded_body = response.body.decode('euc-kr')

        for row in response.css("table.boxstyle02 tbody tr"):

            date = row.css("th a::text").get() or row.css("th::text").get(default="").strip()
            meals = row.css("td")
            breakfast = "No data"
            lunch = "No data"
            dinner = "No data"

            if len(meals) > 0:
                breakfast = "&".join([item.strip() for item in meals[0].css("::text").getall() if item.strip()])
            if len(meals) > 1:
                lunch = "&".join([item.strip() for item in meals[1].css("::text").getall() if item.strip()])
            if len(meals) > 2:
                dinner = "&".join([item.strip() for item in meals[2].css("::text").getall() if item.strip()])

            yield {
                "date": date,
                "breakfast": breakfast,
                "lunch": lunch,
                "dinner": dinner
            }

