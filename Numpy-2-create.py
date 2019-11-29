import numpy as np

arr1 = np.array([[1, 2, 3], [3, 4]])  # 注意： array([1, 2, 3],[3, 4]) is illegal
arr2 = np.array([2, 3], dtype=np.int)   # 可指定类型 int默认为int64位
arr3 = np.zeros((3, 4))  # 创建一个3行4列的全0矩阵
arr4 = np.ones((2, 4), dtype=np.int32 )  #全1
arr5 = np.empty((2, 4))  # 数据为empty不为0 但都接近0
arr6 = np.arange(10, 20, 2)  # 连续数组，步长为2 ：10 12 14 16 18  没有20 shape=(5,)
arr7 = np.arange(12).reshape((3,4))  # reshape 改变数组形状
arr8 = np.linspace(1, 10, 20).reshape(4, 5)   # linspace将数组等分成20个数据的数组
print(arr8)
