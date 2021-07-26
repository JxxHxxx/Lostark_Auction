from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
import numpy

def crawl_data(date, *args):
    legend_grade_price = pd.DataFrame(
                                    columns= ['아이템 명',
                                            '전일 평균 거래가',
                                            '최근 거래가',
                                            '최저가'])
    
    legend_grade_list = []
    for i in args:
        legend_grade_list.append(i)
    # webdriver를 이용하기 위해서는 브라우저 버전에 맞는 driver 를 다운받아야 한다.
    url = "https://lostark.game.onstove.com/Market"

    driver = webdriver.Chrome('C:/Users/JH/Desktop/chromedriver')
    driver.get(url)

    select_item_grade = driver.find_element_by_class_name("grade").click()
    select_legend_grade = driver.find_element_by_xpath("//span[.='전설']").click()

    for i in legend_grade_list:
        txtItemName = driver.find_element_by_id("txtItemName")
        txtItemName.send_keys(i)

        search = driver.find_element_by_class_name("bt").click()
        time.sleep(0.3)

        yesterday_aveg_price = driver.find_element_by_xpath("//td[2]/div[@class='price']/em[@data-grade='0']")
        time.sleep(0.3)
        recently_price = driver.find_element_by_xpath("//td[3]/div[@class='price']/em[@data-grade='0']")
        time.sleep(0.3)
        lowest_price = driver.find_element_by_xpath("//td[4]/div[@class='price']/em[@data-grade='0']")
        time.sleep(0.5)
        legend_grade_price = legend_grade_price.append({'아이템 명' : i,
                                                        '전일 평균 거래가': yesterday_aveg_price.text,
                                                        '최근 거래가' : recently_price.text,
                                                        '최저가': lowest_price.text}, ignore_index= True)

        txtItemName1 = driver.find_element_by_id("txtItemName").clear()

    legend_grade_price.to_csv('C:/Users/JH/Desktop/price/tempo_price_'f'{date}.csv',encoding ='utf-8-sig', index=False)

    driver.quit()
# def exTract 행렬 변환이 필요할 때 (이 함수는 특수한 경우에만 사용됨 extract 이라는 함수를 다시 구성할 필요가 있음)
def exTract(date, col_name):
    df = pd.read_csv('C:/Users/JH/Desktop/price/tempo_price_'f'{date}.csv',encoding ='utf-8-sig', index_col=0)
    transPose_data = df.transpose()
    transPose_data = transPose_data.loc[[col_name],:]
    dataset = pd.DataFrame()
    dataset = transPose_data.to_csv('C:/Users/JH/Desktop/price/dataset_'f'{date}.csv', encoding = 'utf-8-sig')

# def upDate 데이터를 업데이트하고 저장합니다.
def upDate(update_date, read_data, save=None):
    dataset_base = pd.read_csv('C:/Users/JH/Desktop/price/'f'{read_data}.csv',index_col=0)
    dataset_1 = pd.read_csv('C:/Users/JH/Desktop/price/dataset_'f'{update_date}.csv', index_col=0)
    dataset_base = dataset_base.append(dataset_1)

    if save==None:
        dataset_base.to_csv('C:/Users/JH/Desktop/price/'f'{read_data}.csv', mode='w', encoding= 'utf-8-sig')
    else:
        dataset_base.to_csv('C:/Users/JH/Desktop/price/'f'{save}.csv', mode='w', encoding= 'utf-8-sig')
        
# def reName 열의 이름을 변경합니다.
def reName(date, col_name):
    dataset = pd.read_csv('C:/Users/JH/Desktop/price/dataset_'f'{date}.csv',index_col=0)
    dataset = dataset.rename({col_name:date})
    dataset = dataset.to_csv('C:/Users/JH/Desktop/price/dataset_'f'{date}.csv',encoding= 'utf-8-sig')


      
""" def updateData(date,save):
    dataset_base = pd.read_csv('C:/Users/JH/Desktop/price/dataset_merge_recent.csv',index_col=0)
    dataset_1 = pd.read_csv('C:/Users/JH/Desktop/price/dataset_'f'{date}.csv', index_col=0)
    dataset_base = dataset_base.append(dataset_1)
    dataset_base.to_csv('C:/Users/JH/Desktop/price/'f'{save}.csv', mode='w', encoding= 'utf-8-sig')  
 """


""" def extractData_DayPrice(date):
    df = pd.read_csv('C:/Users/JH/Desktop/price/tempo_price_'f'{date}.csv',encoding ='utf-8-sig', index_col=0)
    transPose_data = df.transpose()
    transPose_data = transPose_data.loc[['전일 평균 거래가'],:]
    dataset = pd.DataFrame()
    dataset = transPose_data.to_csv('C:/Users/JH/Desktop/price/dataset_'f'{date}.csv', encoding = 'utf-8-sig')
   
def extractData_RecentPrice(date):
    df = pd.read_csv('C:/Users/JH/Desktop/price/tempo_price_'f'{date}.csv',encoding ='utf-8-sig', index_col=0)
    transPose_data = df.transpose()
    transPose_data = transPose_data.loc[['최근 거래가'],:]
    dataset = pd.DataFrame()
    dataset = transPose_data.to_csv('C:/Users/JH/Desktop/price/dataset_'f'{date}.csv', encoding = 'utf-8-sig') """