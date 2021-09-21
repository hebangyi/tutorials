import numpy as np

# 分割
A = np.arange(12).reshape((3, 4))
print(A)

# 纵向分为2单位进行分割
print(np.split(A, 2, axis=1))
# 横向分为3个单位进行分割
print(np.split(A, 3, axis=0))
# 进行不等项的分割
print("=======")
print(np.array_split(A, 4, axis=0))
