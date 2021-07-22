import pandas as pd

 #데이터셋 베이스는 고정입니다.
dataset_base = pd.read_csv('C:/Users/JH/Desktop/price/dataset_merge.csv',index_col=0)
# 추출한 dataset 을 넣어주세요.
dataset_1 = pd.read_csv('C:/Users/JH/Desktop/price/dataset_20210722.csv', index_col=0)

#dataset_2 = pd.read_csv('C:/Users/JH/Desktop/price/test2.csv', index_col=0)
dataset_base = dataset_base.append(dataset_1)
print(dataset_base)
#dataset_base = dataset_base.append(dataset_2)

dataset_base.to_csv('C:/Users/JH/Desktop/price/dataset_merge.csv', mode='w', encoding= 'utf-8-sig')
# 변경된 데이터만 추가되는게 아니라 데이터 전체가 추가됨

""" dataset_1 = pd.DataFrame({'A': [2000], 'B': [1000]})
print(dataset_1)
dataset_2 = pd.DataFrame({'A':[3000],'B':[2500]})
print(dataset_2)
dataset_1 = dataset_1.append(dataset_2, ignore_index= False)
print(dataset_1)
 """