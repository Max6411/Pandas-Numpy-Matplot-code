import numpy as np

arr1 = np.array([1, 1, 1])  # 一维矩阵叫做向量，没有转置！ shape = (3,)
arr2 = np.array([2, 2, 2])
print(np.vstack((arr1, arr2)))  # 将括号中的两个整体进行vertical合并 array([[1,1,1],[2,2,2]])
print(np.hstack((arr1, arr2)))  # 将括号中的两个整体进行horizontal合并  array([1, 1, 1, 2, 2, 2])

print(arr1[np.newaxis, :])  # array([[1, 1, 1]])  shape = (3,) -> (1, 3) 增加一个维度
print(arr1[:, np.newaxis])  # array([[1],[1],[1]]) shape = (3,) -> (3, 1)

arr3 = arr1[:, np.newaxis]
arr4 = arr2[:, np.newaxis]

print(np.concatenate((arr3, arr4, arr4, arr3), axis=0))  # 多个矩阵合并 axis=0 为列合并 vstack
print(np.concatenate((arr3, arr4, arr4, arr3), axis=1))  # axis=1 按行合并 hstack
