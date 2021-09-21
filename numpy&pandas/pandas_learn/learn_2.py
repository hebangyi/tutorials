import pandas as pd
import numpy as np

datas = pd.date_range('20130131', periods=6)
print(datas)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=datas, columns=['A', 'B', 'C', 'D'])
print(df)

# 选取第A列
print(df['A'], df.A)
# 选取 20130131 - 20130131 的行数据
print(df['20130131':'20130201'])
print(df[0: 2])

# 以标签进行筛选
# 以行标签进行选择
print(df.loc['20130131'])
# 筛选特定行特定列的
print(df.loc['20130131':'20130201', ['A', 'B']])

# 通过位置index选择特定行列
print(df.iloc[3:4, 1:3])
print(df.iloc[[1, 2, 4], 1:3])

# 筛选
print(df[df.A > 8])
# 计算
print(df.A + 8)
