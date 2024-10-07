import scrapy


class DormSpider(scrapy.Spider):
    name = "dorm"
    allowed_domains = ["dorm.kyonggi.ac.kr"]
    start_urls = ["https://dorm.kyonggi.ac.kr:446/Khostel/mall_main.php?viewform=B0001_foodboard_list&gyear=2024&gmonth=10&gday=07"]

    def parse(self, response):
        # euc-kr 인코딩으로 디코딩
        decoded_body = response.body.decode('euc-kr')

        # CSS 선택자 및 데이터 추출
        for row in response.css("table.boxstyle02 tbody tr"):
            datas = [cell.strip() for cell in row.css("td::text").getall() if cell.strip()]
            print(datas)

            datas += ['No data'] * (7 - len(datas))

            yield {
                "sunday": datas[0],
                "monday": datas[1],
                "tuesday": datas[2],
                "wednesday": datas[3],
                "thursday": datas[4],
                "friday": datas[5],
                "saturday": datas[6],
            }
