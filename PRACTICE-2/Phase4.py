# Q1 — Right triangle of numbers, decreasing per row
# Given n, print n rows where row r (1-indexed) prints numbers n down to n-r+1.
# Input: n=4 →
# 4
# 4 3
# 4 3 2
# 4 3 2 1


# n = int(input("Enter a number: "))
# a = n
# k = 0
# for i in range(n):
#     for j in range(k+1):
#         print(n,end=" ")
#         n = n-1
#     k +=1 
#     n = a
#     print()
    
# Q2 — Diamond of a single character
# Given a char and n, print a diamond: widths go 1,3,5,...,2n-1,...,5,3,1.
# Input: ch='*', n=3 →
#   *
#  ***
# *****
#  ***
#   *


# char = input("Enter a single character('*','@','&','$'): ")
# n = int(input("Enter any number you like: "))
# k = 2*n-1
# for i in range(k):
#     for j in range(k):
#        if i < n:
#           if n-i-1<= j <= n+i-1:
#              print(char,end="")
#           else:
#              print(" ",end="")
#        else:
#           if i-n+1 <= j <=k-i+n-2: # this line took a lot of thinking 
#              print(char,end="")
#           else:
#               print(" ",end="")  
#     print()


# Q3 Pattern Problems — warm up first:
# P1 — Staircase of functions (conceptual warmup)
# Print this for n=5:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Each row r prints the number r exactly r times. 
# Build each row as a string, one print per row.

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()


# 2 — Zigzag numbers
# For n=4:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# Continuous counter across rows. Row r has exactly r numbers. 
# No hardcoding the starting number of each row — derive it.
# n = 5
# k = 0
# for i in range(n):
#     for j in range(i+1):
#         print(k+1,end=" ")
#         k = k+1
#     print()

