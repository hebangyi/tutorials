import numpy as np

# 索引练习
A = np.arange(3, 15).reshape((3, 4))
print(A)
# 取出index 为3的索引值
# print(A[3])
print(A[1])
print(A[1][1])

# 使用:
print(A[0][:])
print(A[0][1:3])

for row in A:
    print(row)
    for item in row:
        print(item)


# 转置
for row in A.T:
    print(row)
    for item in row:
        print(item)

for item in A.flat:
    print(item)
