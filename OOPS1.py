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
    college_name = "Mit-Wpu" # we define it outside self because we need 
    #store this data only once... we save a lot of memory this way because 
    #even for thousands of students we need to store the college name only once.
    name = "anonymous" #class attr
    #default constructor..
    def __init__(self):
        pass    
    #parametrized constructor...(We use this generally)
    def __init__(self,name,marks):
        self.name = name  # obj attr >> class attr
        # instance attributes basically they tell us that 
        self.marks = marks # every student in this class has a different name or marks
        print("Showing the name and marks of the student..")
s1 = Student("soham",90)
print(s1.name,s1.marks,Student.college_name)
s2 = Student("tina",92)
print(s2.name,s2.marks,Student.college_name)
