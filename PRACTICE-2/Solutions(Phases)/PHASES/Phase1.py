#question 1
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"{name} is {age} years old.")

#question 2
# num = input("Enter 3 number with spaces")
# num = num.split(" ")
# k =len(num)
# sum = 0
# for i in range(k):
#     sum += int(num[i])
# avg = sum/k
# t = type(avg)
# print(f"Sum: {sum}\nAvg: {avg}\nType of Average: {t}")

#question 3(A very imp trick is in there for avoiding if else statements)
# num = input("Enter a floating point number negative or positive.. ")
# num = num.split(".")
# k = num[0]
# is_negative = k.startswith("-")      # True/False
# sign = ["Positive", "Negative"][is_negative]   # False=0→Positive, True=1→Negative
# integer = int(num[0])
# decimal = round(int(num[1])/(10**len(num[1])),2)
# print(f"Integer Part: {integer}\nDecimal Part: {decimal}\nSign: {sign}")


#question 4(wrong only works for one digit integers)
# a = int(input("Enter a number: "))#7
# b = int(input("Enter a number: "))#3
# print(f"Before swap: a = {a}, b = {b}")
# if a> b:
#     a = str(int((a*b)/a)) + str(a-b)
#     b = int(a[0]) +int(a[1])
#     a = int(a[0])
# else: 
#     a = str(int((a*b)/a)) + str(abs(a-b))
#     b = int(a[0]) - int(a[1])
#     a = int(a[0])
# print(f"After swap: a = {a},b = {b}")

#Simpler and much better version
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# print(f"Before swap: a = {a}, b = {b}")
# a = a + b
# b = a - b
# a = a - b
# print(f"After swap: a = {a}, b = {b}")
