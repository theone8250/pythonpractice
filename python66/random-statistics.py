# 1. 亂數模組 random
# 1.1 隨機選取：choice()、sample()
# 1.2 隨機調換順序：shuffle()
# 1.3 取得隨機亂數：random()、uniform()
# 1.4 取得常態分配亂數：normalvariate()

# 2. 統計模組 statistics
# 2.1 計算平均數：mean()
# 2.2 計算中位數：median()
# 2.3 計算標準差：stdev()

# 隨機模組
import random
# 隨機選取
# data=random.sample([1,5,6,10,20],2)
# print(data)

# 隨機調換順序(洗牌的概念)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

# 隨機取得亂數
# data=random.uniform(60,100) #60~100之間的隨機亂數
# print(data)

# 取得常態分配亂數
# 平均數 100, 標準差 10 得到的資料多數在90~110之間
# data=random.normalvariate(100,10)

# 平均數 0 ,標準差 5,得到的資料多數在-5~5之間
# data=random.normalvariate(0,5)
# print(data)

# 統計模組
import statistics as stat
# data=stat.mean([1,2,3,4,5,8,100]) 平均數
# data=stat.median([1,2,3,4,5,8,100]) 中位數
data=stat.stdev([1,2,3,4,5,8,10]) #標準差
print(data)