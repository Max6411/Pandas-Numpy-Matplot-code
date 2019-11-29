import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.arange(4)  # array([0, 1, 2, 3])
print(arr2 < 3)   # 结果为一个bool型数组 array([True, True, True, flase], dtype为bool)
print(arr2 ** 2)  # array([0, 1, 4, 9]) 幂运算
print(arr1 * arr2)  # array([0, 20, 60, 120])
print(np.dot(arr1, arr2))  # 和print(arr1.dot(arr2)) 相同 dot是数学中的矩阵乘
arr3 = np.random.rand(2, 4)  # 得到一个（2， 4）形状的随机数0-1数组 rand:0-1 randn:0为平均值1为方差 randint(int,int,())
print(np.sum(arr3) , np.max(arr3) , np.min(arr3))  # 整个数组的和， 最大值 以及 最小值
print(np.mean(arr3), np.median(arr3))   #  整个数组的平均值(average) 中位数
arr4 = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
"""
1  2  3  4
5  6  7  8
9 10 11 12
"""
print(np.sum(arr4, axis=0))  # axis指定以行或列划分 0为列1为行 结果： array([15,18,21,24])
print(np.sum(arr4, axis=1))  # array([10,26,42])

print(np.argmin(arr1))  # 输出arr1最小元素的下标:0 argmax则是最大元素的下标：3
print(np.cumsum(arr4))  # 累加函数 array([ 1  3  6 10 15 21 28 36 45 55 66 78])  ndim = 1
print(np.diff(arr4))  # 有累差函数 array( [[1, 1, 1] [1, 1, 1] [1, 1, 1]] )  ndim = ndim(arr4)
arr5 = np.arange(14, 2, -1).reshape((3, 4))
print(np.sort(arr5))  # array([[11,12,13,14],[7,8,9,10],[3,4,5,6]])
print(np.transpose(arr5))  # 矩阵的转置  等于print(arr5.T)
print(arr5.nonzero())  # 输出两个数组 第一个array表示非零元素所在的行，第二个array表示非零元素所在的列
print(np.clip(arr5,5,9))  #  将矩阵中的小于5的值换成5，大于9的值换成9输出
