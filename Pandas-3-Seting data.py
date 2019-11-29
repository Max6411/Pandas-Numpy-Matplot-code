import numpy as np
import pandas as pd

indexdatas = pd.date_range("20191127", periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=indexdatas, columns=['A', 'B', 'C', 'D'])
"""
             A   B   C   D
2019-11-27   0   1   2   3
2019-11-28   4   5   6   7
2019-11-29   8   9  10  11
2019-11-30  12  13  14  15
2019-12-01  16  17  18  19
2019-12-02  20  21  22  23
"""
df.iloc[2, 2] = 11
df.loc['20191129', 'D'] = 22  # 通过loc和iloc直接选取某个元素修改， 和二维数组一样
print(df)
"""
             A   B   C   D
2019-11-27   0   1   2   3
2019-11-28   4   5   6   7
2019-11-29   8   9  11  22  // changed
2019-11-30  12  13  14  15
2019-12-01  16  17  18  19
2019-12-02  20  21  22  23
"""
df.B[df.A > 4] = 0  # 当A列的中元素大于4时， 把这一行B列的元素设为0
df['E'] = 1  # 直接在后面新添一列‘E’ 值都为1
df['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=indexdatas)  # 也可以在后面加上一个序列，但下标要对齐!
print(df)