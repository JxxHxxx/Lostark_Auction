import pandas as pd
import numpy as np

df  = pd.read_csv('C:/Users/JH/Desktop/price/tempo_price_20210721.csv',encoding ='utf-8-sig', index_col=0)
df.info()

transPose_data = df.transpose()
transPose_data = transPose_data.loc[['전일 평균 거래가'],:]
#print(transPose_data)

transPose_data.to_csv('C:/Users/JH/Desktop/price/test2.csv',encoding ='utf-8-sig')