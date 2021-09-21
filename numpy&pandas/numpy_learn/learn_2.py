import numpy as np

# 定义数组中的格式
# 定义一维矩阵 , 加入dtype 参数
a = np.array([2, 23, 4], dtype=np.float)

print(a)
# 输出数据形式
print(a.dtype)

# 定义二维矩阵
b = np.array([[2, 23, 4], [2, 32, 4]])
print(b)

# 定义一个全部为0的二维矩阵
c = np.zeros((3, 4))
print(c)

# 定义一个全部为1的二维矩阵
d = np.ones((3, 4), dtype=float)
print(d)

# 起始值是10 终值是20 生成有序的数列或矩阵,步长是2
print("起始值是10 终值是20 生成有序的数列或矩阵,步长是2")
f = np.arange(10, 20, 2)
print(f)

# 生成十个数的矩阵
f = np.arange(10)
print(f)

# 生成1- 20 分为30个步长的数列
h = np.linspace(1, 20, 30)
print(h)

# 生成1- 20 分为30个步长的数列, 并改变数组结构
i = h.reshape((2, 15))
print(i)
