# #question 1
# # name = "Soham"
# # age = 20
# # city = "Pune"
# # print(f"My name is {name}, I live in {city} and I am {age} years old.")


# #question 2
# num = input("Enter a number: ")
# n = int(num)
# print(f"int: {n}")
# print(f"float: {float(n)}")
# print(f"bool: {bool(n)}")

# #question 3

# name = "programming"
# k = len(name)
# print(f"{name[0]},{name[-1]},{name[k//2]}")

#question 4
# num = int(input("enter a number: "))
# if num > 0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")
    
#question 5
# sentence = input("Enter a sentence: ")
# print(f"{sentence.upper()}\n{len(sentence)}\n{sentence[::-1]}")

#question 6
a = 6
b = 9.9
c = "cat"
d = True
e = [1,2,3]
f = [a,b,c,d,e]
i = 0
for i in f:
    print(i,type(i))
