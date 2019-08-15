import os
from pandas import Series, DataFrame
import pandas as pd
print("-------分割线，数据结构：Series 和 DataFrame-----------")
x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = Series(d)
print(x1)
print(x2)
print(x3)

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [
    65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun',
                             'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)

print("-------分割线，使用 apply 函数对数据进行清洗-----------")
data3 = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df3 = DataFrame(data3, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
# df3['name'] = df3['name'].apply(str.upper)
print(df3)

print("-------分割线，数据统计-----------")
df4 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
print(df4.describe())

print("-------分割线，数据导入和输出-----------")
currentDir = os.path.dirname(__file__)
score = DataFrame(pd.read_excel(currentDir + '/demo1.xlsx'))
score.to_excel(currentDir + '/demo2.xlsx')
print(score)
