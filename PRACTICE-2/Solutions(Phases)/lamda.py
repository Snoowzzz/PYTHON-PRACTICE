## here is the practice of lambda function in python
# Three Real Use Cases

# 1 — With sorted()

# python
# data = [("Soham", 91), ("Riya", 95), ("Arjun", 72)]
# sorted(data, key=lambda x: x[1])  # sort by score
# # → [("Arjun", 72), ("Soham", 91), ("Riya", 95)]

# 2 — With map() — apply a function to every element

# python
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# # → [1, 4, 9, 16]

# 3 — With filter() — keep only elements that match a condition

# python
# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# # → [2, 4, 6]

# practice 1
# temp_in_celsius =[0, 100, 37, -40]
# in_fahr =list(map(lambda x: 9*x/5 + 32,temp_in_celsius))
# print(in_fahr)

# practice 2
# data = [("Soham", 91), ("Riya", 95), ("Arjun", 72)]
# key1 = sorted(data, key=lambda x: (-x[1],x[0])) ## - meaning 
# print(key1)

# practice 3
# Input: ["hi", "cloud", "AWS", "computing", "AI"]
# Output: ["cloud", "computing"]
# data =["hi", "cloud", "AWS", "computing", "AI"]
# data1 = list(filter(lambda x: len(x)>4,data))
# print(data1)

# practice 4
# Input:  ["banana", "apple", "cherry", "date"]
# Output: ["banana", "apple", "date", "cherry"]  ← sorted by a, e, e, y
# fruits = ["banana", "apple", "cherry", "date"]
# fruistnew = sorted(fruits, key=lambda x:x[-1])
# print(fruistnew)

# practice 5
# Input:  ["Soham", "Riya", "Arjun"]
# Output: [("Soham", 5), ("Riya", 4), ("Arjun", 5)]
# name =["Soham", "Riya", "Arjun"]
# newlist = list(map(lambda x: (x,len(x)),name))
# print(newlist)

# practice 6
# # Input:  [1, 2, 3, 4, 5, 6]
# # Output: [4, 16, 36]
# nums =[1, 2, 3, 4, 5, 6]
# newlst = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
# print(newlst)