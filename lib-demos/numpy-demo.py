import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

print("-------分割线-----------")

import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']

print(ages)
print(chineses)
print(maths)
print(englishs)
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

print("-------分割线，统计函数-----------")

x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(x1)
print(x2)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))

print("-------分割线，计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()-----------")
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.amin(a))
print(np.amin(a,0))
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))

print("-------分割线，统计最大值与最小值之差 ptp()-----------")

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))

print("-------分割线，统计数组的百分位数 percentile()-----------")
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

print("-------分割线，统计数组中的中位数 median()、平均数 mean()-----------")
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

print("-------分割线，统计数组中的加权平均值 average()-----------")
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))

print("-------分割线，统计数组中的标准差 std()、方差 var()-----------")
a = np.array([1,2,3,4])
print(np.std(a))
print(np.var(a))
