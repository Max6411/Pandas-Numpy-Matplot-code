import numpy as np
import pandas as pd

indexdatas = pd.date_range("20191127", periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=indexdatas, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan  # numpy中的NAN是一个常数，代表空值
print(df.dropna(axis=0, how='any'))  # 对行进行删除  'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
print(df.fillna(value=0))  # 将表格中的NAN用0替代
"""  以上两个函数都没有修改表格本身  """
print(df.isnull())  # 输出一个bool型表格， nan所在位置为True， 其他地方都是False
print(np.any(df.isnull()))  # 返回一个bool型 判断表格中是否有一个nan值
