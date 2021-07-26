import pandas as pd
import crl
import time

date = 20210727
col_name = '전일 평균 거래가'
save_data = '각인서 일별 평균 거래가'
name_list = ['원한 각인서', '각성 각인서']

crl.crawl_data(date, name_list)
crl.exTract(date, col_name)
crl.reName(date, col_name)
crl.upDate(date, save_data)




