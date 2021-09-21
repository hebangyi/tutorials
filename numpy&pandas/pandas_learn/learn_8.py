import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# 累加操作
data = data.cumsum()

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = data.cumsum()
print(data)
# data.plot()
ax = data.plot.scatter(x='A', y='B', color='Red')
ax = data.plot.scatter(x='A', y='C', color='DarkBlue', ax=ax)

# plt.scatter() bar hist box kde area scatter hexbin pie
plt.show()

