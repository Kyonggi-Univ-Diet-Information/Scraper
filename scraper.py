import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

now = datetime.datetime.now()

year = now.year
month = now.strftime("%m")
day = now.strftime("%d")

url = f'https://dorm.kyonggi.ac.kr:446/Khostel/mall_main.php?viewform=B0001_foodboard_list&gyear={year}&gmonth={month}&gday={day}'

response = requests.get(url)

soup = BeautifulSoup(response.content.decode('euc-kr', 'replace'), 'html.parser')

parsedSoup = soup.select('div > .cate')

print(soup)