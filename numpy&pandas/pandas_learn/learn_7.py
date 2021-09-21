import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
print(df1)
print(df2)
# 有点像Sql的连接方式
# 列连接
print(pd.merge(df1, df2, on='a'))
print(pd.merge(df1, df2, on=['key1', 'key2']))
print(pd.merge(df1, df2, on=['key1', 'key2'], how="outer", indicator=True))

print(pd.merge(df1, df2, left_index=True, right_index=True, how="outer", indicator=True))
