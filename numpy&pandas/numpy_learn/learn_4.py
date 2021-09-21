import numpy as np

# 求出矩阵中最小值的索引
A = np.arange(2, 14).reshape((3, 4))
print("A = ", A)

# 求出最小值的索引
print(np.argmin(A))
# 求出最大值的索引
print(np.argmax(A))

# 求出最小值的索引(列)
print(np.argmin(A, axis=0))
# 求出最小值的索引(行)
print(np.argmax(A, axis=1))

# 求平均值
print("average=", np.average(A))
# 求中位数
print("median=", np.median(A))
# 求出每个值的累加值
print("cumsum=", np.cumsum(A))
# 求出每两个数之间的差值
print("diff=", np.diff(A))
# 输出非零元素的下标
print("nonzero = ", np.nonzero(A))
# 排序
print("sort = ", np.sort(A))
# 矩阵的反向
print("transpose = ", np.transpose(A))
# 取出一个范围的数,如果超过区间,就等于区间值
print("clip=", np.clip(A, 5, 9))\

