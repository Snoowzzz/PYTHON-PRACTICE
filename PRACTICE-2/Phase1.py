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
# print(f"sum: {sum}\navg: {avg}\ntype: {t}")

#question 3
num = input("Enter a floating point number negative or positive.. ")
num = num.split(".")
k = num[0]
sign = k[0]
integer = int(num[0])
decimal = round(int(num[1])/(10**len(num[1])),2)
print(f"IntegerPart: {integer}\nDecimalPart: {decimal}\nSign: {sign}")
