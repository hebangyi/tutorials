import pandas as pd
import numpy as np

# 处理丢失的数据
datas = pd.date_range('20130131', periods=6)
print(datas)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=datas, columns=['A', 'B', 'C', 'D'])
print(df)
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
# 丢掉列
print(df.copy().dropna(axis=1, how='any'))  # {'any', 'all'} any是只要有一个nan
# 填写na默认值
print(df.copy().fillna(value=0))
# 判断是否有na数据
print(df.isnull())
# 是否有一个某值
print(np.any(df.isnull()))
