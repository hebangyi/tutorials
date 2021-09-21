import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print("a=", a)
print("b=", b)
# 矩阵的加法
c = a + b
print("add c = ", c)
# b 的平方
print("square : ", b ** 2)
# 求矩阵的sin值,三角函数
print("sin : ", 10 * np.sin(a))
# 判断矩阵是否为3
print(b == 3)

# 矩阵的乘法运算
c = np.array([[1, 1], [0, 1]])
d = np.arange(4).reshape((2, 2))
# 1)单纯的矩阵中的值逐个相乘
print("矩阵的乘法运算:")
print(c * d)
# 2)矩阵的乘法运算
print(np.dot(c, d))
# print(c.dot(d))

# 随机填写0到1的数字 在一个2行4列的矩阵
rand_a = np.random.random((2, 4))
print("rand_a=", rand_a)

# 将整个矩阵求和
print("sum=", np.sum(rand_a))
# 求出矩阵中的最小值
print("min=", np.min(rand_a))
# 求出矩阵中的最大值
print("max=", np.max(rand_a))
# 求出矩阵中每一列的最小值
print("min2=", np.min(rand_a, axis=0))
# 求出矩阵中每一行的最小值
print("min3=", np.min(rand_a, axis=1))
