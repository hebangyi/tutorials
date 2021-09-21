import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
print(df1)
print(df2)
print(df3)

# 纵向合并
print(pd.concat([df1, df2, df3], axis=0, ignore_index=True))

df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'])
print(pd.concat([df4, df5]))
print(pd.concat([df4, df5], ignore_index=True, join="inner"))

print(df1.append(df2, ignore_index=True))
