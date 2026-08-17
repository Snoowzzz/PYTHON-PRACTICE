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
# Question 1(Reversing a string)
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

# Question 2()
# word = "3,-5,6,-7,-8"
# new_word = word.replace(",","").replace(" ","")
# new_word1 = ""
# k = len(new_word)
# count = 0
# for i in range(k):   
#     if new_word[i] == "-":
#         i = i+2   
#     elif new_word[i] != "-":
#         new_word1 += new_word[i]
#     if new_word[k-2] == "-":
#         count+=1
# if count > 0: 
#     print(new_word1[:k-3])

        