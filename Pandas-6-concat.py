import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['A', 'B', 'C', 'D'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['A', 'B', 'C', 'D'])

res = pd.concat([df1, df2, df3], axis=0)  # 类似np.vstack axis=0是默认参数， 为上下合并
print(res)
res2 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res2)  # 使行下标重新排序而不是将原来的直接放在一起
df4 = pd.DataFrame(np.ones((3, 4))*3, columns=['A', 'B', 'C', 'E'], index=[4, 5, 6])
res3 = pd.concat([df3, df4], axis=0, join='outer')  # join='outer' 是默认参数
print(res3)  # 依照column来做纵向合并，有相同的column上下合并在一起，其他独自的column个自成列，原本没有值的位置皆以NaN填充。
res4 = pd.concat([df3, df4], axis=0, join='inner', ignore_index=True)
print(res4)  # 只有相同的column合并在一起，其他的会被抛弃
res5 = pd.concat([df3, df4], axis=1, join_axes=[df4.index])  # 合并时以df4的索引做标准
print(res5)  # df3若没有这一行则元素值为nan
res6 = df2.append(df3, ignore_index=True)  # 纵向合并 和concat(axis=1,join='outer') 相同
print(res6)
series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res7 = df2.append(series, ignore_index=True)  # APPEND 可以将一个index和column相同的表格上下合并
