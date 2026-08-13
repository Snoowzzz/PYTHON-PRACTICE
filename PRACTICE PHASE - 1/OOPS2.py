# # THis is for practice of OOP in python
# # class Account:
# #     def __init__(self,acc_no,acc_pass):
# #         self.acc_no = acc_no
# #         self.__acc_pass = acc_pass # using the two underscore to hide the attribute ( making it private)
# #     def reset_pass(self):
# #         print(self.__acc_pass)
    
        
# # s1 = Account("Abcd123&yh",8976436)
# # print("THE account name and password are:\n",s1.acc_no,"\n",s1.reset_pass())  #in 
# # #this we display account name and password but it does the actual password gets
# # #printed outside this and in the print statement we see acc name and NONE


# #  IMP INFO REGARDING CALLING A PRIVATE ATTRIBUTES
# class Student:
#     def __init__(self,name):
#         self.name = name
#     def __hello(self):
#         print("Hello person")
#     def welcome(self):
#         print("Oh wait i am seeing someone..",self.__hello())
#         print("Your name is ...",self.name)
        
# s1 = Student("Soham")       
# print(s1.welcome())
      