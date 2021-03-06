from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd

legend_grade_price = pd.DataFrame(
                                columns= ['price'])

# webdriver를 이용하기 위해서는 브라우저 버전에 맞는 driver 를 다운받아야 한다.
url = "https://lostark.game.onstove.com/Market"

driver = webdriver.Chrome('C:/Users/JH/Desktop/chromedriver')
driver.get(url)

legend_grade_list = ['원한','각성','예리한 둔기','정기 흡수']

for i in legend_grade_list:
    txtItemName = driver.find_element_by_id("txtItemName")
    txtItemName.send_keys(i)
    time.sleep(1)
    step1 = driver.find_element_by_class_name("grade").click()
    time.sleep(1)
    step2 =driver.find_element_by_xpath("//span[.='전설']").click()
    time.sleep(1)
    search = driver.find_element_by_class_name("bt").click()
    time.sleep(1)
    price = driver.find_element_by_xpath("//div[@class='price']/em[@data-grade='0']")

    legend_grade_price = legend_grade_price.append({'price': price.text}, ignore_index= True)
  
    print(legend_grade_price)
    time.sleep(1)
    txtItemName1 = driver.find_element_by_id("txtItemName").clear()
    time.sleep(1)
