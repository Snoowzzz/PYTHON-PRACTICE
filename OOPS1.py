# class Student:
#     name = "Soham"
#     age = "20"
# s1 = Student()
# print(f"{s1.name} {s1.age}")
# print(s1.age)

#constuctors in python
class Student:
    def __init__(self):
        print(self)
        print("Adding a new student to the database...")
    name = "Soham"
    age = 20
s1 = Student()
print(s1)