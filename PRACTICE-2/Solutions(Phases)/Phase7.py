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