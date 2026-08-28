### PHASE-7 (OOP + EVERYTHING BEFORE)

### Question 1 (Easy)
# Input:  GradeTracker([88, 92, 79, 95])
# Output: average() -> 88.5
#         highest() -> 95

# class GradeTracker:
#     def __init__(self,grades):
#         self._grades = grades
#     @property
#     def average(self):
#         if len(self._grades) == 0:
#             return None
#         return round(sum(self._grades)/len(self._grades),2)    
#     @property
#     def highest(self):
#         if len(self._grades) == 0:
#             return None
#         k = max(self._grades)
#         return k
# grade = GradeTracker([])
# print(grade.average)
# print(grade.highest)

# ### Question 2 (Easy)
# # Input:  a = ["reading", "gaming", "coding"], 
# #         b = ["gaming", "coding", "cooking"]
# # Output: ["coding", "gaming"]

# def common_interests(a,b):  
#     lstc = set(a)  & set(b)
#     return sorted(list(lstc))

# a = ["reading", "gaming", "coding"]
# b = ["gaming", "coding", "cooking"]
# lst = common_interests(a,b)
# print(lst)

### Question 3 (Medium)
# Input:  books = [Book("Dune", "Herbert", 1965), Book("Neuromancer", "Gibson", 1984),
# Book("1984", "Orwell", 1949)]
# shelf = Shelf(books)
# Output: shelf.sorted_by_year() -> [("1984", 1949),("Dune", 1965),
# ("Neuromancer", 1984)]

# class Book:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
# class Shelf:
#     def __init__(self,books):
#         self.books = books
#     def sorted_by_year(self):
#         lst = []
#         for item in self.books:
#             tupp = (item.title,item.year)
#             lst.append(tupp)
#         modlst = sorted(lst,key=lambda x: (x[1],x[0]))
#         return modlst
# books = [Book("Dune", "Herbert", 1969), Book("Neuromancer", "Gibson", 1984),Book("1984", "Orwell", 1949)]
# shelf = Shelf(books)
# print(shelf.sorted_by_year())

### Question 4 (Medium)
# Input:  w = Wallet(1000)
#         w.spend(200)
# Output: w.spend(200) -> True,  w.balance -> 800
#         w.spend(5000) -> False, w.balance unchanged -> 800

# class Wallet:
#     def __init__(self,balance):
#         self._balance = balance
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self,value):
#         if value < 0:
#             raise ValueError("Enter a positive amount")
#     def spend(self,amount):
#         if amount <= self._balance:
#             self._balance -= amount
#             return True
#         else:
#             return False
# w = Wallet(1000)
# w.spend(200)
# w.spend(200)
# print(w.spend(400))
# print(w.balance)
# # w.spend(1500)
# # print(w.spend())
# # print(w.balance)