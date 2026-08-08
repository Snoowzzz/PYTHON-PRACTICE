# class Student:
#     name = "Soham"
#     age = "20"
# s1 = Student()
# print(f"{s1.name} {s1.age}")
# print(s1.age)

#constuctors in python
# class Student:
#     def __init__(self):
#         print(self)
#         print("Adding a new student to the database...")
#     name = "Soham"
#     age = 20
# s1 = Student()
# print(s1)

#types of consturctors
# class Student:
#     college_name = "Mit-Wpu" # we define it outside self because we need 
#     #store this data only once... we save a lot of memory this way because 
#     #even for thousands of students we need to store the college name only once.
#     name = "anonymous" #class attr
#     #default constructor..
#     def __init__(self):
#         pass    
#     #parametrized constructor...(We use this generally)
#     def __init__(self,name,marks):
#         self.name = name  # obj attr >> class attr
#         # instance attributes basically they tell us that 
#         self.marks = marks # every student in this class has a different name or marks
#         print("Showing the name and marks of the student..")
# s1 = Student("soham",90)
# print(s1.name,s1.marks,Student.college_name)
# s2 = Student("tina",92)
# print(s2.name,s2.marks,Student.college_name)

# how to define a new function and then call it using self 
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def welcome(self):
#         print("Welcome Student",self.name)
#     def get_marks(self):
#         return self.marks
# s1 = Student("Karan",97)
# s1.welcome()
# print(f"You scored {s1.get_marks()} in the last exam..")



# practice from the apni kaksha lecture
# class Student(): 
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks 
#     def average(self,marks):
#         total = sum(marks)
#         average1 = total/len(marks)
#         return average1
# s1 = Student("Soham",[97,96,94])
# k =round(s1.average([97,96,94]),2)
# print(s1.name,s1.marks,k)

# #better version of the upper
# class Student():  
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks 
        
#     @staticmethod  # decorator in python 
#     def hello():   #used to write a function without giving the self parameter
#         print("Hello") #converst a obj attr to class attr
        
#     def average(self):
#         total = sum(self.marks)
#         average1 = total/len(self.marks)
#         print(f"Hi {self.name} your average is {round(average1,2)}")
# s1 = Student("Soham",[97,96,94])
# s1.average()

## Real world scenarion where object oriented is helpful

# class Account:
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self.balance = balance
    
#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Amount {amount} debited, new balance: {self.balance}")
    
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Amount {amount} credited, new balance: {self.balance}")
    
#     def get_balance(self):
#         print("Balance:", self.balance)

# # Usage
# s1 = Account(123678, 10000)
# s1.debit(500)
# s1.credit(12000)
# s1.credit(25000)