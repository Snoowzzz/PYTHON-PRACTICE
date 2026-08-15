# # # THis is for practice of OOP in python
# # # class Account:
# # #     def __init__(self,acc_no,acc_pass):
# # #         self.acc_no = acc_no
# # #         self.__acc_pass = acc_pass # using the two underscore to hide the attribute ( making it private)
# # #     def reset_pass(self):
# # #         print(self.__acc_pass)
    
        
# # # s1 = Account("Abcd123&yh",8976436)
# # # print("THE account name and password are:\n",s1.acc_no,"\n",s1.reset_pass())  #in 
# # # #this we display account name and password but it does the actual password gets
# # # #printed outside this and in the print statement we see acc name and NONE


# # #  IMP INFO REGARDING CALLING A PRIVATE ATTRIBUTES
# # class Student:
# #     def __init__(self,name):
# #         self.name = name
# #     def __hello(self):
# #         print("Hello person")
# #     def welcome(self):
# #         print("Oh wait i am seeing someone..",self.__hello())
# #         print("Your name is ...",self.name)
        
# # s1 = Student("Soham")       
# # print(s1.welcome())
      
# # #Inheritance in python
# # class car:
# #     @staticmethod
# #     def start():
# #         print("Car started..")
# #     @staticmethod
# #     def stop():
# #         print("Car stoped..")
# #     color = "grey"
# # class new_car(car):
# #     def __init__(self,name,model):
# #         self.name = name
# #         self.model = model
# # s1 = new_car("BMW","S+Class")
# # s1.start()
# # print(f"Car name is {s1.name} model is {s1.model}")
# # s1.stop()

# #SUPER METHOD IN PYTHON OOP
# class Car:
#     def __init__(self, type,year):
#         self.type = type
#         self.year = year
    
#     @staticmethod
#     def start():
#         print("car started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name, type,year):
#         super().__init__(type,year)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("prius", "electric",2017)
# print(car1.name,car1.type,car1.year) # always have to use all the statements individually to call
