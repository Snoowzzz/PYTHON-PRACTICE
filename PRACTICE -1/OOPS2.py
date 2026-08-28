# THis is for practice of OOP in python
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass 
#    # using the two underscore to hide the attribute ( making it private)
#     def reset_pass(self):
#         print(self.__acc_pass)
    
        
# s1 = Account("Abcd123&yh",8976436)
# print("THE account name and password are:\n",s1.acc_no,"\n",s1.reset_pass()) 
#    in this we display account name and password but it does the actual password gets
#    printed outside this and in the print statement we see acc name and NONE


# # # # #  IMP INFO REGARDING CALLING A PRIVATE ATTRIBUTES
# # # # class Student:
# # # #     def __init__(self,name):
# # # #         self.name = name
# # # #     def __hello(self):
# # # #         print("Hello person")
# # # #     def welcome(self):
# # # #         print("Oh wait i am seeing someone..",self.__hello())
# # # #         print("Your name is ...",self.name)
        
# # # # s1 = Student("Soham")       
# # # # print(s1.welcome())
      
#Inheritance in python
# class car:
#     @staticmethod
#     def start():
#         print("Car started..")
#     @staticmethod
#     def stop():
#         print("Car stoped..")
#     color = "grey"
# class new_car(car):
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
# s1 = new_car("BMW","S Class")
# s1.start()
# print(f"Car name is {s1.name} model is {s1.model},Colour: {new_car.color}")
# s1.stop()

# # # #SUPER METHOD IN PYTHON OOP
# # # class Car:
# # #     def __init__(self, type,year):
# # #         self.type = type
# # #         self.year = year
    
# # #     @staticmethod
# # #     def start():
# # #         print("car started...")
    
# # #     @staticmethod
# # #     def stop():
# # #         print("car stopped.")

# # # class ToyotaCar(Car):
# # #     def __init__(self, name, type,year):
# # #         super().__init__(type,year)
# # #         self.name = name
# # #         super().start()

# # # car1 = ToyotaCar("prius", "electric",2017)
# # # print(car1.name,car1.type,car1.year) # always have to use all the statements individually to call

# # #class method (changing the value of a class attribute)
# # class Person:
# #     # def changename(self,name):
# #         # Person.name = name #method 1(to change name in the entire class)
# #         # self.__class__.name = "Rahul" 
#           # method 2 (to change name in the entire class only this name is there)
# #     @classmethod # the clean way to change name in the entire class
# #     def changename(cls,name):
# #         cls.name = name
       
# # p1 = Person()
# # p1.changename("Rahul Kumar")
# # print(p1.name)
# # print(Person.name)

# property method(use when the value of a thing is not fixed and 
# needs to be updated instantly)
class Student:
    def __init__(self,phy,cem,math):
        self.phy = phy
        self.cem = cem
        self.math = math
    @property
    def percentage(self):
        # This value is calculated every time it is accessed, so it stays
        # current when phy, cem, or math changes. @property also lets us use
        # attribute syntax (s1.percentage) instead of method syntax.
        k = round((self.phy + self.cem +self.math)/3,2)
        return str(k)+"%"

    # Without @property, percentage could be a regular method:
    # def percentage(self):
    #     return f"{round((self.phy + self.cem + self.math) / 3, 2)}%"
    # Then it would have to be called as s1.percentage(). The result would still
    # be recalculated, but @property makes a derived value look like an attribute.
s1 = Student(98,97,90)
print(s1.percentage)
s1.phy = 86
print(s1.percentage)
s1.math = 80
print(s1.percentage)


# #Polymorphism

# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#     def ShowNum(self):
#         print(self.real ,"i +",self.img,"j")    
#     def __add__(self,s2):       #using the dunder functions in python
#         newreal = self.real + s2.real
#         newimg = self.img + s2.img
#         return complex(newreal,newimg)
#     def __sub__(self,s2):      #using the dunder function in python
#         newreal = self.real - s2.real
#         newimg = self.img - s2.img
#         return complex(newreal,newimg)
# s1 = complex(1,3)
# s1.ShowNum() 
# s2 = complex(2,4)
# s2.ShowNum()
# s3 = s1 + s2  
# s3.ShowNum()
# s4 = s3-s2
# s4.ShowNum()

# Circle Def practice question 1
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         area = round(math.pi*(self.radius**2),2)
#         print(area)
#     def perimeter(self):
#         peri = round(math.pi*(self.radius),2)
#         print(peri)
# s1= Circle(8)
# s1.area()
# s1.perimeter()


# question 2
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def Showdetails(self):
#         print(f"Employee role: '{self.role}'\nDepartment: '{self.department}'\nSalary: '{self.salary}$'")
# class Engineer(Employee):
#     Employee.role ="Engineer"
#     def __init__(self,name,age,workingExp):
#         self.name = name
#         self.age = age
#         self.workingExp = workingExp
#         super().__init__("Engineer","IT","75000")
#     def PersonalInfo(self):
#         print("PERSONAL INFO  \nName: ",self.name)
#         print("Age: ",self.age)
#         print("Experience: ",self.workingExp)
                
# eng1 = Engineer("Vikrant",27,4) 
# eng1.Showdetails()
# eng1.PersonalInfo()


#Practice 3(Use dunder fuction to compare)
# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price
#     def __gt__(self,order2): # dunder function of compare(>)
#         if self.price>order2.price:
#             return "order1>order2"
#         return "order2>order1"
# order1 = Order("Pizza",17)
# order2 = Order("Burger&Fries",16)
# print(order1.__gt__(order2)) 