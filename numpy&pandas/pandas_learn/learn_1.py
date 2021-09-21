import pandas as pd
import numpy as np

# 创建一维数
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

datas = pd.date_range('20210101', periods=6)
print(datas)

# 生成一个带标题的名称
print(pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['a', 'b', 'c', 'd']))

df = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df)
print("=======")
print(df.dtypes)
print("=======")
# 输出序号
print(df.index)
# 输出行
print(df.columns)

# 描述功能
print(df.describe())
# 矩阵转换功能
print(df.T)
# 排序功能,以行为单位
print(df.sort_index(axis=1, ascending=False))
# 排序功能,根据索引字段0排序
print(df.sort_values(by=0,ascending=False))
