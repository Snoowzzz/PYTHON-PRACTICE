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

## Question 3
# Input:  [("Soham", 91), ("Riya", 95), ("Soham", 88), ("Arjun", 72), ("Riya", 97)]
# Output: [("Riya", 97), ("Soham", 91), ("Arjun", 72)]

# def leaderboard(score):
#     scoreboard =[]
#     for i in range(len(score)):
#         for j in range(len(score)):
#             if i!= j:
#                 if score[i][0] == score[j][0]:
#                     t = max(score[i][1],score[j][1])
#                     tupp = (score[i][0],t)
#                     scoreboard.append(tupp)
#                 else:
#                     tupp = (score[i])
                    
# score =[("Soham", 91), ("Riya", 95), ("Soham", 88), ("Arjun", 72), ("Riya", 97)]
# print(leaderboard(score))

## Question 4 (audit)

# # Output: {
#     "present":    {"Soham", "Riya", "Arjun"},
#     "absent":     {"Meera"},
#     "gate_crash": {"Karan"}
# }
def audit(registered,attended):
    present = set()
    absent = set()
    gatecrash = set()
    for i in registered:
        if i in attended:
            present.add(i)
        else:
            absent.add(i)
    for j in attended:
        if j not in registered:
            gatecrash.add(j)
    dictaudit = {
        "present": present,
        "absent": absent,
        "gate_crash": gatecrash,
    }
    return dictaudit
registered = ["Soham", "Riya", "Arjun", "Meera"]
attended   = ["Soham", "Arjun", "Karan", "Riya"]
print(audit(registered,attended))