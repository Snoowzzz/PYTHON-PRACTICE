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
class Student:
    
    #default constructor..
    def __init__(self):
        pass
    
    #parametrized constructor...(We use this generally)
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Showing the name and marks of the student..")

s1 = Student("soham",90)
print(s1.name,s1.marks)

s2 = Student("tina",92)
print(s2.name,s2.marks)