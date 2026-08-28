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

# Q6) Create a class Book with __init__(self, title, author, pages). 
# Add a __str__ method so print(book) outputs: 
# "<title> by <author> (<pages> pages)".
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def __str__(self):  ## now we
# book = Book("Three Body Problem", "Cixin Liu", 567)
# print(book)


#### Session 2
### PHASE — OOP: Inheritance & super()
##### Notes ########
# class Parent:
#     def __init__(self, x):
#         self.x = x
#     def greet(self):
#         return f"Parent has {self.x}"

# class Child(Parent):                    # Child inherits from Parent
#     def __init__(self, x, y):
#         super().__init__(x)             # let Parent set up self.x
#         self.y = y                      # Child adds its own attribute
#     def greet(self):                    # overrides Parent's greet()
#         return f"Child has {self.x} and {self.y}"
# s1 = Parent("Child")
# s2 = Child("Child","Sansa")
# print(s1.greet())
# print(s2.greet())


# Q1. Create a class Vehicle with __init__(self, brand, speed). Create a
#     class Car(Vehicle) that inherits from it, using super().__init__()
#     for brand and speed, and adds its own attribute doors. Add a method
#     info() on Car returning "<brand> car with <doors> doors, top speed <speed>."
# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def info(self):
#         return f"This {self.brand} car has a top speed of {self.speed}"
# class Car(Vehicle):
#     def __init__(self,brand,speed,model,doors):
#         # Problem: `super` is the built-in function that gives access to the
#         # parent class, but here it is referenced without being called.
#         # Therefore, `super.__init__` tries to access `__init__` on the
#         # built-in `super` object itself instead of accessing Vehicle's
#         # initializer. The parent initializer is consequently not executed,
#         # so `self.brand` and `self.speed` are not set for this Car object.
#         super().__init__(brand,speed)
#         self.model = model
#         self.doors = doors
#     def info(self):
#         return f"Model {self.model} of {self.brand} car with {self.doors} doors.\nThis car has a top speed of {self.speed}Km/h"
# s1 = Vehicle("Mercedes",280)
# s2 = Car("Mercedes",320,"AMG","Carbon-Fibre")   
# print(s1.info())  
# print(s2.info())
        
# Q2. Create a class Shape with a method area() that returns 0. Create
#     Square(Shape) with __init__(self, side) and an overridden area()
#     returning side ** 2.
# class Shape:
#     @staticmethod
#     def area(radius):
#         return 3.14 * (radius)**2
# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#     def area(self):
#         return (self.side)**2
# s1 = Shape()
# print(s1.area(9))
# s2 = Square(8)
# print(s2.area())

# Q3. Create a class Person with __init__(self, name, age) and a method
#     intro() returning "<name>, <age> years old.". Create Student(Person)
#     that inherits from it, adds roll_no via its own __init__ (using
#     super() for name/age), and overrides intro() to return
#     "<name>, <age> years old, Roll No: <roll_no>."

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         return f"{self.name}, {self.age} years old."
# class Student(Person):
#     def __init__(self,name,age,rollno):
#         super().__init__(name,age)
#         self.rollno = rollno
#     def intro(self):
#         return f"{super().intro()} Roll No: {self.rollno}" ## important
# s1 = Person("Soham",20)
# print(s1.intro())
# s2 = Student("Soham",20,48)
# print(s2.intro())

# Q4. Create a class Employee with __init__(self, name, salary) and a
#     method details() returning "<name> earns <salary>.". Create
#     Manager(Employee) that inherits, adds team_size via super(), and
#     overrides details() to return
#     "<name> earns <salary> and manages <team_size> people."

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def details(self):
#         return f"{self.name} earns {self.salary}"
# class Manager(Employee):
#     def __init__(self,name,salary,team_size):
#         super().__init__(name,salary)
#         self.teamsize = team_size
#     def details(self):
#         return f"{super().details()} and manages {self.teamsize} people."
# s1 = Employee("Karan",90000)
# print(s1.details())
# s2 = Manager("Sachin",150000,24)
# print(s2.details()) 
 
# Q5. Create a class Animal with __init__(self, name) and a method sound()
#     returning "Some generic sound." Create two subclasses, Cat(Animal)
#     and Bird(Animal), each overriding sound() — Cat returns
#     "<name> says Meow.", Bird returns "<name> says Tweet." No new
#     attributes needed in the children, just super().__init__(name).
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound():
#         return "Some generic sound."

# class Cat(Animal):
#     def sound(self):
#         return f"{self.name} says Meow."

# class Bird(Animal):
#     def sound(self):
#         return f"{self.name} says Tweet."

# s1 = Cat("Minny")
# s2 = Bird("Andy")
# print(s1.sound())
# print(s2.sound())

# Solution using super() in the child classes:
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         return "Some generic sound."

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         return f"{self.name} says Meow."

# class Bird(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         return f"{self.name} says Tweet."

# s3 = Cat("Minny")
# s4 = Bird("Andy")
# print(s3.sound())
# print(s4.sound()) can call the class directly
#         return f"{self.title} by {self.author} ({self.pages} pages)"
#---------------------------------------------------------------------------------------------
### extending practice of oop

## Question 1
# Input:  t = Temperature(100)
# Output: t.fahrenheit -> 212.0
# class Temperature:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     @property
#     def fahrenheit(self):
#         return (9 * self.celsius) / 5 + 32
# t = Temperature(100)
# print(t.celsius)
# print(t.fahrenheit)  
# ## property makes derived value fahrenheit look like a attribute

## Question 2
# Input:  p = Person("Soham", "Kulkarni")
# Output: p.full_name -> "Soham Kulkarni"
# class Person:
#     def __init__(self,first_name,last_name):
#         self.firstname = first_name
#         self.lastname = last_name
#     @property
#     def fullname(self):
#         return f"{self.firstname} {self.lastname}"
# p = Person("Soham","Kulkarni")
# print(p.fullname)

## Question 3
# Input:  p = Product(100)
#         p.price = 150
# Output: p.price -> 150

# Input:  p.price = -20
# Output: raises ValueError
# class Product:
#     def __init__(self,price):
#     # The underscore shows that _price is an internal/backing attribute;
#     # it also prevents the property setter from recursively calling itself.
#         self._price = price
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self,value):
#         if value < 0:
#             raise ValueError("Price can't be negative..")
#         self._price = value
# p = Product(100)
# print(p.price)

## Question 4
# Input:  c = Circle(5)
# Output: c.area -> 78.53975

# Input:  c.radius = -3
# Output: raises ValueError
# class Circle:
#     def __init__(self,radius):
#         self._radius = radius
#     @property
#     def area(self):
#         return round(22/7 * (self._radius**2),3)
#     @area.setter
#     def area(self,value):
#         if value < 0:
#             raise ValueError("Radius can't be negative")
#         self._radius = value
# c = Circle(5)
# print(c.area)

# Explanation:
# `@property` is needed to make `area` readable like an attribute:
# `c.area` instead of `c.area()`.
#
# `@area.setter` is optional. It is only needed when we want to allow an
# assignment such as `c.area = value`. However, a setter must belong to an
# existing property, so `@area.setter` cannot be used by itself.
#
# The two functions have different jobs:
# - the property getter returns or calculates the area;
# - the setter validates and handles a value assigned to `c.area`.
#
# In this code, the setter changes `_radius`, so the assigned value is really
# treated as a radius, even though it is assigned through `area`. A clearer
# design is to make a separate `radius` property if the radius should be set:
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError("Radius can't be negative")
#         self._radius = value
#
# Properties are not compulsory: a normal `get_area()` method can be used,
# but then it must be called with parentheses: `c.get_area()`.

### Question 5
# Input:  e = Employee("Riya", 50000)
# Output: e.annual_salary -> 600000

# Input:  e.salary = 60000
# Output: e.annual_salary -> 720000
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self._salary = salary
#     @property
#     def salary(self):
#         return self.salary
#     @salary.setter
#     def salary(self,value):
#         if value < 0 :
#             raise ValueError("Salary can't be negative")
#         self._salary = value
#     @property
#     def annualsalary(self):
#         return self._salary*12
# e = Employee("Riya",50000)
# print(e.annualsalary)
# e.salary = 60000
# print(e.annualsalary)

class CreditCard:
    def __init__(self, number, balance):
        self._number = number      # full number stored internally
        self._balance = balance

    @property
    def number(self):
        # getter transforms the raw stored value before exposing it
        return "**** **** **** " + self._number[-4:]
    @number.setter
    def number(self,value):
        if len(value) != 16:
            raise ValueError("Card number should be of 16 digit")
        self._number = value
    @property
    def balance(self):
        # getter formats a raw float into a display-ready string
        return f"${self._balance:,.2f}"

card = CreditCard("4532015112830366", 15420.5)
print(card.number)  
# **** **** **** 0366  ← never exposes the real number
card.number = "9999"
print(card.number)   
# $15,420.50            ← formatted, not the raw float

