# import math
# def fact(n1 ,n2 ):
#     n1 = math.factorial(n1) 
#     n2 = math.factorial(n2)
#     print(n1,n2,sep=",")
# fact(5,8)

# def d(n):
#     d={}
#     for i in range (1,n+1) :
#         d[i] = i*i
#     print(d)
# d(8)

# def cou(str1) :
#     numcou= 0 
#     charcou = 0
#     for i in len(str1):

# str1 = input("enter the string")
# print(cou(str1))

import numpy as np 
# arr = np.arange(1,10)
# print(arr)

# arr1 = np.random.rand(5)
# arr2 = np.random.rand(5)
# print(arr1) 
# print(arr2)

# mat = np.random.rand(3,3)
# print(mat)

# arr1 = np.random.rand(5)
# arr2 = np.random.rand(5)
# print(arr1 @ arr2)


# mat = np.eye(5)
# print(mat)

# def cou(str1) :
#     numcou= 0 
#     charcou = 0
#     l = []
#     for i in str1 :
#         l.append(i)
#     print(l)
#     for i in range(len(l)) :
#         try :
#             l[i] = int(l[i])
#         except :
#             pass
#     for i in l :
#         if i ==" ":
#             charcou -= 1
#         if isinstance(i,int):
#             numcou += 1 
#         if isinstance(i,str):
#             charcou += 1
#     print(numcou , charcou)
# str1 = input("enter the string ")
# print(cou(str1))

# def x (str1):
#     str1 = str1.split(" ")
#     print(str1)
#     str1 = set(str1)
#     str1 = list(str1)
#     str1 = str1.sort()
#     print(str1)
#     " ".join(str1)
#     return (str1)
# print(x("hello world and practice makes perfect and hello world again"))

# import pandas as pd
# df = pd.read_csv("C:\Users\omare\OneDrive\Desktop\train (1).csv",sep= ",")