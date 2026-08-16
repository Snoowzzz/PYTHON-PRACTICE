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
# a = 6
# b = 9.9
# c = "cat"
# d = True
# e = [1,2,3]
# f = [a,b,c,d,e]
# i = 0
# for i in f:
#   print(i,type(i))

#question 7
# word = input("Enter a word: ")
# if len(word) <= 5:
#     print("Too short to split")
# else:
#     k = len(word)//2
#     print(f"{word[:k]}\n{word[k:]}")

#question 8 (GOOD Question)
# h = input("Enter anything: ")
# if "." in h:   #remember this
#     k = h.replace(".","",1)  #remember this
#     if len(k) == 0 or k =="-":
#         print("string") 
#     elif k[0] != "-":
#         if k.isdigit():
#             print("float")
#         else:
#             print("string")
#     else:
#         if k[1:].isdigit():
#             print("float")
#         else:
#             print("string")
# else:
#     if h[0] != "-":
#         if h.isdigit():
#             print("int")
#         else:
#             print("string")
#     else:
#         if h[1:].isdigit():
#             print("int")
#         else:
#             print("string")
          
# question 9
# name = input("Enter you full name: ")
# h = name.split(" ")
# print(f"{h[1]}, {h[0]}")
# k = h[0]
# t = h[1]
# print(f"{k[0].upper()}.{t[0].upper()}.")
# name_new = name.replace(" ","")
# print(len(name_new))

#question 11 (Pretty good)
# word = input("Enter any word: ")
# vowels = ["a","e","i","o","u"]
# word1 = word.lower()
# for i in range(5):
#     if vowels[i] in word1:
#         print(f"{vowels[i]}: {word1.count(vowels[i])}") # super important

# HARD QUESTIONS:( mine was wrong still working on it)
# strnumber = input("Enter two number you want to perform operation on in the form 'a +-/* b: ")
# operator = ["+","-","/","*"]
# for i in range(4):
#     strnum = strnumber.replace(" ","")
#     if operator[i] in strnum[1:]:
#         strnew = strnum.split(operator[i],1)
#         if i == 0:
#             result = int(strnew[0]) + int(strnew[1])
#         elif i == 1:
#             result = int(strnew[0]) - int(strnew[1])
#         elif i == 2:
#             result = float(int(strnew[0]) / int(strnew[1]))
#         elif i == 3:
#             result = int(strnew[0]) * int(strnew[1])
# print(result)

# BETTER SOLUTION
# strnumber = input("Enter expression (e.g. '12 + 5'): ")
# parts = strnumber.split(" ")   # split on spaces → ["12", "+", "5"]
# a = parts[0]
# op = parts[1]
# b = parts[2]

# # smart casting
# def cast(x):
#     if "." in x:
#         return float(x)
#     return int(x)

# num1 = cast(a)
# num2 = cast(b)

# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "*":
#     result = num1 * num2
# elif op == "/":
#     if num2 == 0:
#         print("Division by zero")
#         result = None
#     else:
#         result = num1 / num2
# else:
#     print("Invalid operator")
#     result = None

# if result is not None:
#     if isinstance(result, float) and result == int(result) and op != "/":
#         print(int(result))
#     else:
#         print(result)




