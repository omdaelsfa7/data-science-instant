# l1 =[]
# _remove = int(input("Enter the wanted to remove number: "))
# for i in range(5):
#     l1.append(int(input("Enter the elements of the list: ")))
# print(l1)    
# while _remove in l1 :
#     if _remove == l1[i] :
#         l1.pop(i)
# print(l1)  
         
# size = int(input("Enter the size of the list: "))
# is_imposter = True
# imposter_index = 0
# l1 = []
# for i in range(size):
#     l1.append(int(input("Enter the list item: ")))
# imposter = int(input("Enter the number to check is exist: "))
# if imposter in l1:
#     pass
# else:
#         is_imposter = False
# while is_imposter in l1 :
#     imposter_index=l1.index(imposter)
#     break
# print(l1)
# if is_imposter:
#     print("imposter index is ",imposter_index)
# else :
#     print("the number do not exist")

# l1 =[]
# max_num = 0
# max_index = 0 
# size = int(input("Enter the size of the list: "))
# for i in range(size) :
#     l1.append(int(input("Enter list elements: ")))
# min_num = l1[0]
# min_index = 0     
# for i in l1 :
#     if i>= max_num :
#         max_num = i
#         max_index = l1.index(i) 
#     if i<= min_num :
#         min_num = i
#         min_index = l1.index(i)
# print("l1 before update",l1)
# l1[max_index] , l1[min_index] = l1[min_index] , l1[max_index]
# print("l1 after update",l1)
# print ("min value %d min index %d , max value %d max index %d"  % (min_num , min_index , max_num , max_index))

# A = []
# size = int(input("Enter the list size: "))
# for i in range(size):
#     A.append(int(input("Enter list elements: ")))
# min_value = A[0]
# min_index = 0 
# for i in A :
#     if i <= min_value :
#         min_value = i
#         min_index = A.index(i)
# print(A)
# print("min value = %d , min value index is = %d" %(min_value,min_index))

# A= []
# size = int(input("Enter the list size : "))
# for i in range (size):
#     A.append(int(input("Enter the list elements: ")))
# A.sort()
# print (A)
# str1 = input("Enter the string: ")
# def space_remover(str1):
#     for i in range(len(str1)):
#         str1 = str1.replace(" ","")
#     return str1    
# print(space_remover(str1))   
# l1 = []
# size = int(input("Enter the size of the list: "))
# for i in range(size):
#     l1.append(int(input("Enter the list elements: ")))
# def swap(l1):
#     l1[0] , l1[-1] = l1[-1] , l1[0]
#     return l1 
# print(swap(l1))
# x = int(input("Enter a number: "))
# q = int(input("Enter a number: "))
# z = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# m = str(x*q*z*y)
# print(m[-2::])
# l1 = [1,1,1,2,3,4,5,5,6]
# l1.sort()
# min_odd = 0
# for i in l1 :
#     if i%2 != 0 :
#         min_odd

def Fibonacci( number):
    if (number <= 1):
        return number
    else:
        return (Fibonacci(number - 2) + Fibonacci(number - 1))
print(Fibonacci(13))