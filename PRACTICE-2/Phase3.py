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