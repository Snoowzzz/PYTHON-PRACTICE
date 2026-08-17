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
number = int(input("Enter any number: "))
if number%2 !=0:
    for i in range(number-1,0,-2):
        print(i,end=" ")  #first time using this pretty good
else:
    for i in range(number,0,-2):
        print(i,end=" ") #first time using this pretty good
        

