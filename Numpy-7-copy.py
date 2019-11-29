import numpy as np
arr1 = np.arange(4)
arr2 = arr1
arr1[0] = 10
print(arr2)  # [10 1 2 3]  默认的赋值方式是浅复制
arr3 = arr1.copy()
arr1[0] = 0
print(arr3)  # [10 1 2 3]  copy过来的就是深复制
