# # Question 1 (Calculates the sum of n numbers: )
# number = int(input("Enter a number: "))
# total = 0
# for i in range(number,0,-1):
#    total+= i
# print(total)
 
 
# # Question 2
# s = input("Enter any string: ")
# for i in range(len(s)):
#     print(f"{i}: {s[i]}")
    
# Question 3
# number = int(input("Enter any number: "))
# if number%2 !=0:
#     for i in range(number-1,0,-2):
#         print(i,end=" ")  #first time using this pretty good
# else:
#     for i in range(number,0,-2):
#         print(i,end=" ") #first time using this pretty good

#Question 3 (cleaner version)
# number = int(input("Enter any number: "))
# start = number if number % 2 == 0 else number - 1
# for i in range(start, 0, -2):
#     print(i, end=" ")
        
        
# Question 4
# n = int(input("Enter countdown start time: "))
# while n>=0:
#     if n == 0:
#         print("Liftoff!")
#         n-=1
#         break
#     else:
#         print(n)
#         n-=1

# Question 4 (cleaner version)
# n = int(input("Enter countdown start time: "))
# while n > 0:
#     print(n)
#     n -= 1
# print("Liftoff!")

# MEDIUM ONES
# Question 1 (Reversing a string)
# word = input("Enter any word: ")
# k = len(word)
# rev_word = ""
# for i in range(k-1,-1,-1):
#     rev_word+=word[i]
# print(rev_word)

# #another way of doing it
# # for i in range(0,k):
# #     rev_word+=word[k-i-1]
# print(rev_word)

# Question 2 (Print the sum of positive numbers in a string: )
# word = input("Enter any numbers separated by comma or space: ")
# new_word = word.replace(",","").replace(" ","")
# k = len(new_word)
# i = 0
# total = 0
# while i < k:  #Important learning whenever we have to skip something
#     if new_word[i] == "-":  # in a loop use while not for
#         i +=2
#     else:
#         total += int(new_word[i])
#         i+=1
# print(total)   
    
    

# Question 3 (print a letter n+1 number of times where n = index)
# word = input("Enter a word: ")
# for i in range(len(word)):
#     print(word[i]*(i+1))

# another approach for this
# word = input("Enter a word: ")
# for pos, ch in enumerate(word):
#     # pos gives the index/position of each character
#     # ch is the actual character at that position
#     print(ch * (pos + 1))


#Question 4 (Print the highest digit in a number)
# number = int(input("Enter a number: "))
# k = abs(number)
# word = str(k)
# a = 0
# for pos in word:
#     if int(pos) > a:
#         a = int(pos)
#     else:    # writing this cause felt good
#         pass
# print(f"Largest digit: {a}")

# Question 5 (Find if a certain range contains a number multiple of 15)
# print("Enter the range in which you want to find (a,b)")

# Better way of taking two inputs in one sentence
# Type two numbers separated by a space (e.g., 10 20)
# num1, num2 = map(int, input("Enter two numbers: ").split())
# print("First number:", num1)
# print("Second number:", num2)

# a = int(input("Enter the first value a: "))
# b = int(input("Enter the second value b: "))
# for i in range(a,b+1):
#     if i%15 == 0:
#         print(i)
#         break
# else:
#     print("None found")

# Question 6 (Check if a string has numbers)
# word = input("Enter a word: ")
# for pos in word:
#     if pos.isdigit():
#         print("Contains digit")
#         break
# did not wrote the else cause u did not ask for it..

# Question 7 (factorial using While)
# n = int(input("Enter a number (Positive): ")) 
# fact = 1
# if n == 0 or n == 1:
#    print(1,"(Odd)") 
# else:
#     while n>=2:
#         fact *= n
#         n = n-1
#  print(fact,"(Even)") #any number greater than 1 has a even factorial..
   
    
    
# Hard ones
# Hard (4) 
# # Input: "aaabbbcca" → Output: "a3b3c2a1"
string1 = "aaabbbbcd"
k = len(string1)
t = 1
newstr = ""

for i in range(k - 1):          # stop one early, no i+1 crash
    if string1[i] == string1[i + 1]:
        t += 1
    else:
        newstr += string1[i]
        newstr += str(t)
        t = 1

# last group always needs manual flush — this is what you were missing
newstr += string1[-1]
newstr += str(t)

print(newstr)   # a3b4c1d1
# Q2 — Nested Loops + Operators (accumulator)
# Print a triangle of running sums (triangular numbers), n rows.
# Input: "4" → Output: "1\n1 3\n1 3 6\n1 3 6 10"
# n =int(input("Enter a number: "))
# k = 0
# p  = 0
# for i in range(0,n):
#     for j in range(0,i+1):
#         p+=1
#         print(k+p,end=" ")
#         k = k+p
#     k = 0
#     p = 0
#     print()


# Hard question 4
# Given "rows,cols", print a mini multiplication table, space-separated.
# Input: "3,3" → Output: "1 2 3\n2 4 6\n3 6 9"
# k = 1
# i = int(input("Enter the now of rows: "))
# j = int(input("Enter the no of coloumns: "))
# for rows in range(i):
#     for cols in range(j):  #this line decides number of times you want to print
#         print((rows+1)*k,end=" ") # something in line....
#         k+=1
#     k = 1
#     print()

# Hard question 3
# H3 — Loops + Strings + If-Else
# Balanced-parentheses check with a running counter (single bracket type, no imports).
# Input: "(a+(b*c)-d)" → Output: "Balanced"
# Input: "(a+b))" → Output: "Not Balanced"
# equation = "(a+(b-c()))"
# k = len(equation)
# count = 0
# for value in equation:
#     if value == "(":
#         count += 1
#     elif value == ")":
#         count -= 1
#     if count < 0:
#         break
# print("Balanced" if count == 0 else "Not Balanced")