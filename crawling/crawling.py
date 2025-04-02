from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9A%B4%EC%84%B8')
time.sleep(1)

# 성별 선택 값
# sex = 'M'
sex_btn_1 = driver.find_element(By.XPATH,'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[1]/div/a')
sex_btn_1.click()

if sex == 'M':
    sex_btn_2 = driver.find_element(By.XPATH,'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[1]/div/div/ul/li[1]/a')
    sex_btn_2.click()
elif sex == 'F':
    sex_btn_2 = driver.find_element(By.XPATH,'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[1]/div/div/ul/li[2]/a')
    sex_btn_2.click()

year_type_btn_1 = driver.find_element(By.XPATH,'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[2]/div/a')
year_type_btn_1.click()
year_type_btn_2 = driver.find_element(By.XPATH,'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[2]/div/div/ul/li[1]/a')
year_type_btn_2.click()

time_btn_1 = driver.find_element(By.XPATH,'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[3]/div/a')
time_btn_1.click()

# 시간 선택 값(1~13)
# time_sel = 1
time_btn_1 = driver.find_element(By.XPATH,f'//*[@id="fortune_birthCondition"]/div[1]/div[1]/div[3]/div/div/ul/li[{time_sel}]/a')
time_btn_1.click()

date_btn_1 = driver.find_element(By.XPATH,f'//*[@id="fortune_birthCondition"]/div[1]/div[2]/a')
date_btn_1.click()


# 연도 선택 1940~2025
# year_sel = 2000 - 1939
year_btn_1 = driver.find_element(By.XPATH, f'//*[@id="fortune_birthCondition"]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/ul/li[{year_sel}]/a')
year_btn_1.click()

# 1~12
# month_sel = 2
month_btn_1 = driver.find_element(By.XPATH, f'//*[@id="fortune_birthCondition"]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/ul/li[{month_sel}]/a')
month_btn_1.click()

# 1~31
# day_sel = 3
day_btn_1 = driver.find_element(By.XPATH, f'//*[@id="fortune_birthCondition"]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/div/ul/li[{day_sel}]/a')
day_btn_1.click()

start_btn = driver.find_element(By.XPATH, '//*[@id="fortune_birthCondition"]/div[1]/button')
start_btn.click()
time.sleep(1)

total_short = driver.find_element(By.XPATH, '/*[@id="fortune_birthResult"]//div[1]/dl[1]/dd/strong').text
total_long = driver.find_element(By.XPATH, '//*[@id="fortune_birthResult"]/div[1]/dl[1]/dd/p').text
love_long = driver.find_element(By.XPATH, '//*[@id="fortune_birthResult"]/div[1]/dl[2]/dd/p').text
money_long = driver.find_element(By.XPATH, '//*[@id="fortune_birthResult"]/div[1]/dl[3]/dd/p').text
health_long = driver.find_element(By.XPATH, '//*[@id="fortune_birthResult"]/div[1]/dl[6]/dd/p').text
