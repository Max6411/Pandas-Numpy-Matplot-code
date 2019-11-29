import numpy as np

arr1 = np.arange(12).reshape((3, 4))
"""
array([ [0, 1, 2, 3]
        [4, 5, 6, 7]
        [8, 9, 10, 11] ])
"""
print(np.split(arr1, 2, axis=1))
"""  axis=1 为按列分割为2个数组
[ array([ [0, 1]      array([ [2, 3]
          [4, 5]              [6, 7]
          [8, 9] ])           [10, 11] ]) ]
"""
print(np.split(arr1, 3, axis=0))  # 等于 np.vsplit(arr1, 3) 竖砍
"""  axis=0 按列分割 必须等量平分
[ array([ [0, 1, 2, 3] ]) array([ [4, 5, 6, 7] ]) array([ [8, 9, 10, 11] ]) ]
"""
print(np.array_split(arr1, 3, axis=1))  # 等于 np.hsplit(arr1, 3)  横砍
"""  普通的分割会报错 不等分只能用array_split 尽量往平分结果靠近 前面的长度不小于后面
[ array([ [0, 1]      array([ [2]     array([ [3]
         [4, 5]              [6]             [7]
         [8, 9] ])           [10] ])         [11] ]) ]  最外层还有一对方括号，结果只有一个对象
"""
