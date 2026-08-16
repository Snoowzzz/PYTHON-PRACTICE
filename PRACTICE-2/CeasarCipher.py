## THIS IS MY SELF BUILT ON FIRST ATTEMPT CAESAR CIPHER
# HARD PROBLEM 2 (Super Important)
# Q12 — Caesar Cipher
# Take a string and a shift number as input. Shift every alphabet character forward by shift positions (wrap around after z). Non-alphabet characters stay unchanged. Case must be preserved.

# Example: "Hello, World!" with shift 3 → "Khoor, Zruog!"

import string
letters = str(string.ascii_letters)
lowercase = str(string.ascii_lowercase)
uppercase = str(string.ascii_uppercase)
sentence = input("Enter anything: ")
L = len(sentence)
shift = int(input("How many words you want to shift: "))
newsentence = ""
# newsentence += "abc"
# print(newsentence)
for i in range(L):
    if sentence[i] in letters:
        if sentence[i].isupper():
            k = uppercase.find(sentence[i]) #returns the index of the position
            t = k+3
            t = (k+shift)%26
            newsentence += uppercase[t]
        else: 
            k = lowercase.find(sentence[i]) #returns the index of the position
            t = k+3
            if t > 25:
                t -= 26
            newsentence += lowercase[t]
    else:
        newsentence += sentence[i]

print(newsentence)