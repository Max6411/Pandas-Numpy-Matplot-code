import pandas as pd
import numpy as np

s = pd.Series([1, 2, 4, np.nan, 16])  # np.nan是一个在numpy中的特殊数值
print(s)  # 会自动输出索引，从0开始
"""
0     1.0
1     2.0
2     4.0
3     NaN
4    16.0
dtype: float64
"""
datas = pd.date_range("20160101", periods=6)  # 连续的6个日期作为表格的行索引
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['a', 'b', 'c', 'd'])  # 数据， 行索引， 列索引
print(df)  # 二维表格
"""
                   a         b         c         d
2016-01-01  1.191910 -0.329401  1.076041  0.195931
2016-01-02 -0.688134  0.230204 -1.841763 -0.676101
2016-01-03 -0.430083 -0.795258  1.125756  0.290944
2016-01-04 -0.214166 -1.437197 -0.449093 -1.439969
2016-01-05  1.056507 -0.984152 -0.308846  1.298760
2016-01-06 -1.203513 -0.639349  0.403508 -1.251569
"""
print(df['b'])  # 以DateFrame形式输出某一列(行不行)的数据 =print(df.b)
df2 = pd.DataFrame(np.arange(12).reshape(3, 4))  # 未给出行索引和列索引 则索引默认从0开始
df3 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})  # 也可以自己一列一列地输入
print(df3)
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
print(df3.dtypes)  # 以列为单位输出每列的形式
print(df3.index)  # 输出DateFrame的行索引
print(df3.columns)  # 列索引
print(df3.values)  # 只输出值不输出行索引和列索引
print(df3.describe())  # 一次性输出整个表格的总结/描述
print(df3.T)  # 也可以连上索引行像矩阵那样转置
print(df2)
print(df2.sort_index(axis=1, ascending=False))  # 排序整条索引 axis=1 为以整列为单位 ascending等于false为值倒序排序
print(df2.sort_values(by=2, ascending=False))  # 排序第“2”列的值
