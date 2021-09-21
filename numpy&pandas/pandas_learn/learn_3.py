import pandas as pd
import numpy as np

datas = pd.date_range('20130131', periods=6)
print(datas)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=datas, columns=['A', 'B', 'C', 'D'])
print(df)

# 定位改变值
df.iloc[2, 2] = 1111
print(df)

df.loc['20130131', 'B'] = 2222
print(df)
# 判断与整体赋值
df.B[df.A > 4] = 0
print(df)
# 新加一个数列
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=datas)
print(df)
