# def x (str1):
#     str1 = str1.split(" ")
#     str1 = set(str1)
#     str1 = list(str1)
#     str1.sort()
#     str1 = " ".join(str1)
#     return (str1)
# print(x("hello world and practice makes perfect and hello world again"))

import pandas as pd
df = pd.read_csv("C:\\Users\\omare\\OneDrive\\Desktop\\gui\\train.csv",sep= ",")
# print(df.head(5))
# print(df.corr())
# newdf = df.nunique()
# print(newdf)
# import numpy as np
# arr1 = np.random.rand(5)
# arr2 = np.random.rand(5)
# print(np.hstack((arr1,arr2)))