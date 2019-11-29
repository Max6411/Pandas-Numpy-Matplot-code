import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on='key')  # 将两个表格合并，依据时key中的重复项
print(res)
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on=['key1', 'key2'], how='right')  # 默认的how时inner 还有'left' 和 'right'
print(res)  # left和right 合并组的数据完全取决与其中某一个
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
print(df2)
"""     
df1:
   col1 col_left
0     0        a
1     1        b
df2:
   col1  col_right
0     1          2
1     2          2
2     2          2
"""
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)  # indicator=True会将合并的记录放在新的一列。
res2 = pd.merge(df1, df2, on='col1', how='outer', indicator='new_column')  #  可以自定义新行的名字 默认是_merge
"""
   col1 col_left  col_right  new_column
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
"""


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
"""
left:
#     A   B    
# K0  A0  B0  
# K1  A1  B1
# K2  A2  B2
right:
#     C   D
# K0  C0  D0
# K2  C2  D2
# K3  C3  D3
"""

res3 = pd.merge(left, right, left_index=True, right_index=True, how='outer')  # 简单的左右outer合并

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

#使用suffixes解决overlapping的问题
res4 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res4)
"""  若还有其他列的名字相同，可以用suffixes重新分配两个名字
    k  age_boy  age_girl    
0  K0        1         4
1  K0        1         5
"""