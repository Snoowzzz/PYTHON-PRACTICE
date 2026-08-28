## THIS IS MY SELF BUILT FIRST ATTEMPT of CAESAR CIPHER
# HARD PROBLEM 2 (Super Important)
# Q12 — Caesar Cipher
# Take a string and a shift number as input. Shift every alphabet character forward by shift positions (wrap around after z). Non-alphabet characters stay unchanged. Case must be preserved.

# Example: "Hello, World!" with shift 3 → "Khoor, Zruog!"

# import string

# letters = string.ascii_letters
# lowercase = string.ascii_lowercase
# uppercase = string.ascii_uppercase

# sentence = input("Enter anything: ")
# shift = int(input("Shift by how many positions: "))
# newsentence = ""

# for char in sentence:
#     if char in letters:
#         if char.isupper():
#             k = uppercase.find(char)
#             newsentence += uppercase[(k + shift) % 26]
#         else:
#             k = lowercase.find(char)
#             newsentence += lowercase[(k + shift) % 26]
#     else:
#         newsentence += char

# print(newsentence)

# def caesar_cipher(word,k,mode):
#      newstr = ""
#      if mode == "encode":
#         for i in word:
#             if i.isupper():
#               if ord(i)+k%26 > 90:
#                 t = ord(i)+(k%26) - 26 # 
#                 newstr+=chr(t)
#               else:
#                 t = ord(i)+(k%26)
#                 newstr+=chr(t)
#             elif i.islower():
#               if ord(i)+k%26 > 122:
#                 t = ord(i)+(k%26) - 26 # 
#                 newstr+=chr(t)
#               else:
#                 t = ord(i)+(k%26)
#                 newstr+=chr(t) 
#             else:
#                 newstr+=i      
#      elif mode == "decode":
#         for i in word:
#             if i.isupper():
#               if ord(i)-k%26 < 65:
#                 t = ord(i)-(k%26) + 26 # 
#                 newstr+=chr(t)
#               else:
#                 t = ord(i)-(k%26)
#                 newstr+=chr(t)
#             elif i.islower():
#               if ord(i)-k%26 < 97:
#                 t = ord(i)-(k%26) + 26 # 
#                 newstr+=chr(t)
#               else:
#                 t = ord(i)-(k%26)
#                 newstr+=chr(t) 
#             else:
#                 newstr+=i  
#      else:
#         print("Enter a Valid Mode: ")
#      return newstr
# word = input("Enter any word: ")
# k = int(input("How many words would u like to shift: "))
# mode = input("Enter a mode (encode or decode): ")
# print(caesar_cipher(word,k,mode))