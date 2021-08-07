# ver2.4 까지 사용했던 time.sleep은 대규모 데이터를 처리해야할 때 매우 느리고 슬립을 느슨하게 잡아주지 않으면 attach error 가 발생하는 경우가 많았음
# WebDriverWait 의 명시적 대기를 사용해 속도와 안정성을 올림

# 인터넷 환경에 따라 다르지만 time.sleep 을 사용했을 때 각인서 하나당 데이터를 불러오는데 최소 1.4초의 타임슬립을 부여해야 했음
# ver2.6의 경우 sleep 이 0.1초가 잡혀있음 ver2.4와 비교해 1.3초 감소, 현재 리스트의 길이는 59, 59*1.3 절약, 즉 76.3초를 절약


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import time
import pandas as pd
import numpy
import matplotlib.pyplot as plt


def crawl_data(date, args=None):
    legend_grade_price = pd.DataFrame(
                                    columns= ['아이템 명',
                                            '전일 평균 거래가',
                                            '최근 거래가',
                                            '최저가'])
    
    legend_grade_list = []

    if args==None:
        list = ['원한 각인서','각성 각인서','예리한 둔기 각인서','정기 흡수 각인서','고독한 기사 각인서','화력 강화 각인서','절실한 구원 각인서','진화의 유산 각인서',
            '잔재된 기운 각인서','극의: 체술 각인서','절정 각인서','피스메이커 각인서','상급 소환사','일격필살 각인서','초심 각인서','분노의 망치 각인서',
            '멈출 수 없는 충동 각인서','돌격대장 각인서','축복의 오라 각인서','기습의 대가 각인서','죽음의 습격 각인서','두 번째 동료 각인서','황후의 은총 각인서',
            '역천지체 각인서','중력 수련 각인서','슈퍼 차지 각인서','갈증 각인서','충격 단련 각인서','바리케이드 각인서','넘치는 교감 각인서','전투 태세 각인서',
            '결투의 대가 각인서','절제 각인서','광전사의 비기 각인서','사냥의 시간 각인서','중갑 착용 각인서','아르데타인의 기술 각인서','세맥타통 각인서','심판자 각인서',
            '오의난무 각인서','광기 각인서','완벽한 억제 각인서','버스트 각인서','오의 강화 각인서','진실된 용맹 각인서','황제의 칙령 각인서','핸드거너 각인서',
            '연속 포격 각인서','안정된 상태 각인서','타격의 대가 각인서','질량 증가 각인서','추진력 각인서','시선 집중 각인서','속전속결 각인서','전문의 각인서','긴급구조 각인서',
            '정밀 단도 각인서','구슬동자 각인서','최대 마나 증가 각인서']  
        
        for i in list:
            legend_grade_list.append(i) 
    else:                        
        for i in args:
            legend_grade_list.append(i) 
            
    url = "https://lostark.game.onstove.com/Market"
    driver = webdriver.Chrome('C:/Users/JH/Desktop/chromedriver')
    driver.get(url)
    
    driver.find_element_by_class_name("grade").click()
    driver.find_element_by_xpath("//span[.='전설']").click()

    for i in legend_grade_list:
        txtItemName = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID,"txtItemName")))
        txtItemName.send_keys(i)
        print("success send key")

        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 
        "button.button.button--deal-submit")))[0].click()
        print("success click")
        # 타임슬립을 걸지 않으면 attached error 발생
        time.sleep(0.1)
        yesterday_aveg_price = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//td[2]/div[@class='price']/em[@data-grade='0']")))
        recently_price = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//td[3]/div[@class='price']/em[@data-grade='0']")))
        lowest_price = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH,"//td[4]/div[@class='price']/em[@data-grade='0']")))
        
        legend_grade_price = legend_grade_price.append({'아이템 명' : i,
                                                        '전일 평균 거래가': yesterday_aveg_price[0].text,
                                                        '최근 거래가' : recently_price[0].text,
                                                        '최저가': lowest_price[0].text}, ignore_index= True)

        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.ID, "txtItemName")))[0].clear()
        print("success clear")
        
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

# 아이템들의 변화율을 시각화 합니다.
