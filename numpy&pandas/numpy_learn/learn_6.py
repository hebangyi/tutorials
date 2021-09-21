import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# 上下合并
C = np.vstack((A, B))
print(C)
print(C.shape)

# 左右合并
D = np.hstack((A, B))
print(D)
print(D.shape)

# 使用坐标轴合并(纵向合并)
print(np.concatenate((A[:, np.newaxis], B[:, np.newaxis]), axis=1))

# 添加一个行维度
print(A[np.newaxis, :])

# 添加一个列维度
print(A[:, np.newaxis])
