# ### PHASE 6

# ### Question 1 Easy
# # Input:  "  Hello   WORLD  how  ARE you  "
# # Output: "hello world how are you"
# def clean_string(word):
#     newstr = ""
#     count = 0
#     for i in word:
#         if i != " ":
#            newstr += i
#            count+=1
#            continue
#         if count>0 :
#             newstr+=" "
#         count = 0
                
#     ### cleaner way 
#         if i != " ":
#            if count == 0 and newstr != "":  #start of new word,not the first word
#                 newstr += " "
#            newstr += i
#            count += 1
#         else:
#             count = 0
        
#     modstr = newstr.lower()
#     return modstr
# word ="  Hello   WORLD  how  ARE you   "
# newword = clean_string(word)
# print(newword)

## QUESTION 2 (MEDIUM)
# Input:  ["name", "age", "city"], ["Soham", 21, "Pune"]
# Output: {"name": "Soham", "age": 21, "city": "Pune"}

# Input:  ["a", "b", "c"], [1, 2]
# Output: {"a": 1, "b": 2}

# def zip_to_dict(keys,values):
#     k = len(keys)
#     v = len(values)
#     d = {}
#     t = min(k,v)
#     for i in range(t):
#         d[keys[i]] = values[i]          
#     return d

# keys =["a", "b", "c"]
# values = ["Soham", 21, "Pune"]
# zip_dict = zip_to_dict(keys,values)
# print(zip_dict)