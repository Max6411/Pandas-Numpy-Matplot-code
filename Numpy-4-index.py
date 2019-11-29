import numpy as np

arr1 = np.arange(3, 15)
print(arr1[1])  # 4
arr2 = arr1.reshape(3, 4)
print(arr2[2])  # array([11,12,13,14])
print(arr2[1:3, 1:3])  # array([[8 ,9],[12,13]])  数组的切片操作 1,2行1,2列
for raw in arr2:
    print(raw)  # 一行一行地输出数组
for column in arr2.T:
    print(column)  # 转逆矩阵后一列一列地输出数组
print(arr2.flatten())  # 将多维数组展开成一维数组
for item in arr2.flat:
    print(item)  # flat是多维数组的迭代器，逐一打印出所有的元素。
