import pandas as pd

datas = pd.read_csv("student.csv")  # 可读取的格式有 csv, excel, json, pickle
print(datas)  # 会自动加上索引
datas.to_pickle('Student.pickle')  # 若目标文件不存在则会在当前目录创建一个文件
