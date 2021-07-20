from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd

legend_grade_price = pd.DataFrame(
                                columns= ['아이템 명',
                                        '전일 평균 거래가',
                                        '최근 거래가',
                                        '최저가'])

legend_grade_list = ['원한 각인서',
                    '각성 각인서',
                    '예리한 둔기 각인서',
                    '정기 흡수 각인서',
                    '고독한 기사 각인서',
                    '화력 강화 각인서',
                    '절실한 구원 각인서',
                    '진화의 유산 각인서',
                    '잔재된 기운 각인서',
                    '극의: 체술 각인서',
                    '절정 각인서',
                    '피스메이커 각인서',
                    '상급 소환사',
                    '일격필살 각인서',
                    '초심 각인서',
                    '분노의 망치 각인서',
                    '멈출 수 없는 충동 각인서',
                    '돌격대장 각인서',
                    '축복의 오라 각인서',
                    '기습의 대가 각인서',
                    '죽음의 습격 각인서',
                    '두 번째 동료 각인서',
                    '황후의 은총 각인서',
                    '역천지체 각인서',
                    '중력 수련 각인서',
                    '슈퍼 차지 각인서',
                    '갈증 각인서',
                    '충격 단련 각인서',
                    '바리케이드 각인서',
                    '넘치는 교감 각인서',
                    '전투 태세 각인서',
                    '결투의 대가 각인서',
                    '절제 각인서',
                    '광전사의 비기 각인서',
                    '사냥의 시간 각인서',
                    '중갑 착용 각인서',
                    '아르데타인의 기술 각인서',
                    '세맥타통 각인서',
                    '심판자 각인서',
                    '오의난무 각인서',
                    '광기 각인서',
                    '완벽한 억제 각인서',
                    '버스트 각인서',
                    '오의 강화 각인서',
                    '진실된 용맹 각인서',
                    '황제의 칙령 각인서',
                    '핸드거너 각인서',
                    '연속 포격 각인서',
                    '안정된 상태 각인서']

# webdriver를 이용하기 위해서는 브라우저 버전에 맞는 driver 를 다운받아야 한다.
url = "https://lostark.game.onstove.com/Market"

driver = webdriver.Chrome('C:/Users/JH/Desktop/chromedriver')
driver.get(url)

select_item_grade = driver.find_element_by_class_name("grade").click()
select_legend_grade =driver.find_element_by_xpath("//span[.='전설']").click()

for i in legend_grade_list:
    txtItemName = driver.find_element_by_id("txtItemName")
    txtItemName.send_keys(i)

    search = driver.find_element_by_class_name("bt").click()
    time.sleep(0.1)

    yesterday_aveg_price = driver.find_element_by_xpath("//td[2]/div[@class='price']/em[@data-grade='0']")
    time.sleep(0.1)
    recently_price = driver.find_element_by_xpath("//td[3]/div[@class='price']/em[@data-grade='0']")
    time.sleep(0.1)
    lowest_price = driver.find_element_by_xpath("//td[4]/div[@class='price']/em[@data-grade='0']")
    time.sleep(0.2)
    legend_grade_price = legend_grade_price.append({'아이템 명' : i,
                                                    '전일 평균 거래가': yesterday_aveg_price.text,
                                                    '최근 거래가' : recently_price.text,
                                                    '최저가': lowest_price.text}, ignore_index= True)

    txtItemName1 = driver.find_element_by_id("txtItemName").clear()

print(legend_grade_price)

legend_grade_price.to_csv('C:/Users/JH/Desktop/price/tempo_price_20210721.csv',encoding ='utf-8-sig', index=False)
#금일 날짜를 적어주세요 시간은 14시 기준