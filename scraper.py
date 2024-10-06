from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import datetime
import time

now = datetime.datetime.now()

year = now.year
month = now.strftime("%m")
day = now.strftime("%d")

url = f'https://dorm.kyonggi.ac.kr:446/Khostel/mall_main.php?viewform=B0001_foodboard_list&gyear={year}&gmonth={month}&gday={day}'

driver_path = "/usr/bin/safaridriver"
driver = webdriver.Safari(driver_path)

driver.get(url)
time.sleep(3)

table = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table[2]')

rows = table.find_elements(By.XPATH, './/tr')

for row_idx, row in enumerate(rows):
    print(f"--- Row {row_idx + 1} ---")
    cells = row.find_elements(By.XPATH, './/th | .//td')  # th와 td 모두 찾기
    for cell_idx, cell in enumerate(cells):
        print(f"Cell {cell_idx + 1}: {cell.text.strip()}")
    print()

driver.quit()