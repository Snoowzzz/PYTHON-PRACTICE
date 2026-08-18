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
char = "*"
n = 3

for i in range(n):
    for j in range(5):
        for j in range(n-i-1,n+i-1):
            print(char,end="")
        else:
            print(" ",end="")
    print()