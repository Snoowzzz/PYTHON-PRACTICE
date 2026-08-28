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
#         return round(sum(self._grades)/len(self._grades),2)
#     @average.setter
#     def average(self,value):
#         if len(value) == 0:
#             raise ValueError("List can't be empty")
#         self._grades = value
#     @property
#     def highest(self):
#         k = max(self._grades)
#         return k
# grade = GradeTracker([88, 92, 79, 95])
# print(grade.average)
# print(grade.highest)
