from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

path = '/Users/재욱/Downloads/chromedriver'
driver = webdriver.Chrome(path, options=options)
# driver.implicitly_wait(3)

driver.get('https://www.naver.com/')
time.sleep(1)
# send_keys 방법이 Capture system 에 막힘
# driver.find_element_by_name('id').send_keys('dlsdj132')
# driver.find_element_by_name('pw').send_keys('qkekrkwk132')

xpath = '//a[@class="link_login"]'
xpath_id = '//input[@id="id"]'
xpath_pw = '//input[@id="pw"]'
xpath_login = '//input[@id="log.login"]'

my_id = 'dlsdj132'
my_pw = 'qkekrkwk132'
# 로그인 클릭
driver.find_element_by_xpath(xpath).click()
# id 복사 및 붙여넣기
pyperclip.copy(my_id)
driver.find_element_by_xpath(xpath_id).send_keys(Keys.CONTROL, 'v')
# pw 복사 및 붙여넣기
pyperclip.copy(my_pw)
driver.find_element_by_xpath(xpath_pw).send_keys(Keys.CONTROL, 'v')
# 로그인 클릭
driver.find_element_by_xpath(xpath_login).click()
time.sleep(1)

# Naver Pay 접속 
driver.get('https://order.pay.naver.com/home')

xpath_item = '//*[@id="_rowLi20210624192803CHK2021062435863661"]'
print(driver.find_elements_by_xpath(xpath_item))


item_xpath = '//*[@id="_listContentArea"]'
division = driver.find_element_by_xpath(item_xpath)
item_list = division.find_elements_by_tag_name('li')

item_id_list = []
for item in item_list:
    
    id = item.get_attribute('id')
    print(id)
    if id != '':
        item_id_list.append(id)

from pprint import pprint
pprint(item_id_list)