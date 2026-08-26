### This file covers the practice of Object Oriented Programming
### in python (Very Important topic)

# Q1. Create a class Student with __init__(self, name, age). 
#     Add a method introduce() that returns 
#    "Hi, I'm <name> and I'm <age> years old."
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         return f"Hi, I'm {self.name} and I'm {self.age} years old."
# s1 = Student("Soham",20)
# print(s1.introduce())

# 2) Create a class Rectangle with __init__(self, width, height). 
# Add area() returning width × height, and perimeter() returning 
# 2×(width+height).
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.height * self.width
#     def perimeter(self):
#         return 2*(self.height +self.width)
# s1 = Rectangle(25,15)
# print(f"Area: {s1.area()},Perimeter: {s1.perimeter()}")

# 3) Q3. Create a class Counter with instance attribute count starting
# at 0.Add increment() (adds 1), reset() (sets back to 0), and
# get_count() (returns current count).

# class Counter:
# #     # A class attribute belongs to the class itself and is shared by all
# #     # instances. It is defined directly inside the class, outside methods.
# #     # Example: every Counter object could read Counter.counter.
# #     # Use a class attribute for data that should be common to every object.
# #     # counter = 0

#     def __init__(self):
#         # An instance attribute belongs to one particular object. It is
#         # usually created with self inside __init__, so each object gets its
#         # own independent value.
#         # Use an instance attribute for data that can differ between objects.
#         self.count = 0

#     def increment(self):
#         self.count += 1

#     def reset(self):
#         self.count = 0

#     def get_count(self):
#         return self.count


# # Example usage:
# first = Counter()
# second = Counter()
# first.increment()
# first.increment()
# print(first.get_count())   # 1
# print(second.get_count())  # 0; each object has its own instance attribute

# # Class attributes are accessed through the class or an instance:
# # Counter.counter = 10
# # print(Counter.counter)     # shared class-level value

# Q4.Create a class Dog with a class attribute species = "Canine" and 
# instance attributes name and breed. 
# Add describe() returning "<name> is a <breed>. Species: <species>." — 
# pull species from the class, don't hardcode it in the string.
# class Dog:
#     species = "Canine"
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#     def describe(self):
#         return f"{self.name} is a {self.breed}.Species: {Dog.species}"
# s1 = Dog("Andrew","German Shepherd")
# print(s1.describe())

# Q5) Create a class BankAccount with __init__(self, owner, balance=0). 
# Add deposit(amount) (adds to balance) and withdraw(amount) 
# (subtracts from balance, but never let it go negative — return False on 
#  insufficient funds, True on success).
# class BankAccount:
#     def __init__(self,owner,balance = 0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance+= amount
#     def withdraw(self,amount):
#         if self.balance - amount < 0:
#             print(f"{False} .. Insufficient Funds")
#         else:
#             self.balance -= amount
#             print(f"{True}.. Withdrawal was a Success")
#     def checkbalance(self):
#         return self.balance
# s1 = BankAccount("Tina") 
# s1.deposit(5000)
# print(s1.checkbalance())
# s1.deposit(10000)
# print(s1.checkbalance())
# s1.withdraw(3000)
# print(s1.checkbalance())
# s1.withdraw(14000)
# print(s1.checkbalance())

            