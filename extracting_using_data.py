import pandas as pd
import numpy as np

#추출한 tepo data를 넣어주세요
df = pd.read_csv('C:/Users/JH/Desktop/price/tempo_price_20210723.csv',encoding ='utf-8-sig', index_col=0)

transPose_data = df.transpose()
transPose_data = transPose_data.loc[['전일 평균 거래가'],:]

#print(transPose_data)
dataset = pd.DataFrame()
# dataset 날짜 기입하세요
dataset = transPose_data.to_csv('C:/Users/JH/Desktop/price/dataset_20210723.csv', encoding = 'utf-8-sig')
#print(dataset)

#newdata = pd.DataFrame()
#newdata = pd.read_csv('C:/Users/JH/Desktop/price/test2.csv', encoding= 'utf-8-sig', index_col= 'Unnamed: 0')
#print(newdata)


 

#transPose_data.to_csv('C:/Users/JH/Desktop/price/test.csv' ,mode='a', encoding ='utf-8-sig')
