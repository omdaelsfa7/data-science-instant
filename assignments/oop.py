# # class person :
# #     def __init__(self,name,gender,age):
# #         self.__name = name
# #         self.__gender = gender 
# #         self.__age = age 
# #     def _set_name(self,name):
# #         self.__name = name
# #     def _set_gender(self,gender):
# #         self.__gender = gender 
# #     def _set_age(self,age):
# #         self.__age = age
# #     def _get_name(self):
# #         return self.__name
# #     def _get_gender(self):
# #         return self.__gender 
# #     def _get_age(self):
# #         return(self.__age)
# #     def __str__(self):
# #         return(f"your name {self.__name}, your gender {self.__gender}, your age {self.__age}")
# # class student(person):
# #     def __intit__(self,name,gender,age,level,gpa,dep,id):
# #         super().__init(self,name,gender,age,level,gpa,dep,id)
# #         self.__level = level 
# #         self.__gpa = gpa 
# #         self.__dep = dep 
# #         self.__id = id  
# #     def _set_level(self,level):
# #         self.__level = level
# #     def _set_gpa(self,gpa):
# #         self.__gpa = gpa
# #     def _set_dep(self,dep):
# #         self.__dep = dep
# #     def _set_id(self,id):
# #         self.__id = id      
# #     def _get_level(self):
# #         return(self.__level)
# #     def _get_dep(self):
# #         return(self.__dep)
# #     def _get_id(self):
# #         return(self.__id)
# #     def __str__(self):
# #         return f"your name {self.get_name()}"

# class o:
#     def __init__(self,):
#         self.__to_do = []
#     def setter(self,to_do):
#         self.__to_do = to_do

#     def add_task(self,x):
#         self.__to_do.append(x)
#         print(self.__to_do)

#     def delete(self,x):
#         if x in self.__to_do :
#             self.__to_do.remove(x)
#             print(self.__to_do) 
#         else :
#             print("task is not in the list")
#             print(self.__to_do)   

#     def show_to_do(self):
#         print(self.__to_do)

#     def mark(self,x):
#         if x in self.__to_do :
#             self.__to_do[self.__to_do.index(x)] = "done"
#             print(self.__to_do)
# o1 = o()
# o1 = o()
# o1.setter(["play","omda","elsfa7"])
# o1.add_task(input("enter what u want to add: "))
# o1.delete(input("enter what u want to delete: "))
# o1.mark(input("enter what u want to mark: "))
# # o1.show_to_do()