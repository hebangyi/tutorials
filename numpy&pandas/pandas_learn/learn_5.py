# pandas 读取文件
import pandas as pd
data = pd.read_csv('student.csv')

# 文件保存
data = pd.to_pickle('student.pickle')
