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

## Question 3 ( Really elegant solution self made)
# Input:  [("Soham", 91), ("Riya", 95), ("Soham", 88), ("Arjun", 72), ("Riya", 97)]
# Output: [("Riya", 97), ("Soham", 91), ("Arjun", 72)]

# def leaderboard(score):
#     d = {}
#     list1 = []
#     for info in score:
#         a,b = info
#         if a not in d.keys():
#             d[a] = b
#         else:
#             k = d[a]
#             if b > k:
#                 d[a] = b
#     for i,v in d.items():
#        tupp = (i,v) 
#        list1.append(tupp)
#     list2 = sorted(list1,key=lambda x: -x[1]) 
#     return list2
    
                    
# score =[("Soham", 91), ("Riya", 95), ("Soham", 88), ("Arjun", 72), ("Riya", 97)]
# print(leaderboard(score))

## Question 4 (audit)

# # Output: {
#     "present":    {"Soham", "Riya", "Arjun"},
#     "absent":     {"Meera"},
#     "gate_crash": {"Karan"}
# }
# def audit(registered,attended):
#     present = set()
#     absent = set()
#     gatecrash = set()
#     for i in registered:
#         if i in attended:
#             present.add(i)
#         else:
#             absent.add(i)
#     for j in attended:
#         if j not in registered:
#             gatecrash.add(j)
#     dictaudit = {
#         "present": present,
#         "absent": absent,
#         "gate_crash": gatecrash,
#     }
#     return dictaudit
# registered = ["Soham", "Riya", "Arjun", "Meera"]
# attended   = ["Soham", "Arjun", "Karan", "Riya"]
# print(audit(registered,attended))

## Question 5 Lambda Pipeline

# lists= [
#     {"name": "Soham", "score": 91},
#     {"name": "Riya",  "score": 45},
#     {"name": "Arjun", "score": 67},
#     {"name": "Meera", "score": 78}
# ]
# passed = list(filter(lambda x: x["score"]>=50,lists))
# grades = list(map(lambda x: (x["name"], "A" if x["score"] >= 75 else "B"), passed)) ##
# ## important line in grade very useful trick
# print(grades)

## Question 6 (analyse_text)
# Input:  "the cat sat on the mat the cat"
# Output: {
#     "word_count": 8,
#     "unique_words": {"the", "cat", "sat", "on", "mat"},
#     "most_frequent": "the",
#     "avg_word_length": 3.0
# }

# def analyse_text(word):
#     cword = word.replace(" ","")
#     newword = word.split(" ")
#     wordcount = len(newword)
#     unique = set()
#     list1 = []
    
#     freq = round(len(cword)/wordcount,2)
#     for i in newword:
#         unique.add(i)
#         k = newword.count(i)
#         list1.append(k)
#     lst2 = list(sorted(set(list1), reverse=True)) ## just for fun
#     for i in newword:
#         k = newword.count(i)
#         if k == lst2[0]:
#             mostrep = i
#     textdict = {
#         "word_count": wordcount,
#         "unique_words": unique,
#         "most_frequent": mostrep,
#         "avg_word_length": freq,
#     }
#     return textdict
# word = "the cat sat on the mat the cat"
# dict1 = analyse_text(word)
# print(dict1)

# ## Question 7 (list a-b without using sets)
# # Input:  a = [1, 2, 3, 4, 5], b = [2, 4]
# # Output: [1, 3, 5]

# # Input:  a = [1, 1, 2, 3], b = [1]
# # Output: [2, 3]   ← both 1s removed
# def list_diff(a,b):
#     newlst = []
#     for i in a:
#         if i not in b:
#             newlst.append(i)
#     return newlst
# a = [1, 1, 3, 4]
# b = [1]
# print(list_diff(a,b))

# ## Question 8 (hard problem)
# def add_student(book,name,scores):
#     if len(book) == 0:
#         average = sum(scores)/len(scores)
#         dict1 ={
#         "name": name,
#         "scores": scores,
#         "average": average,
#         }
#         book.append(dict1)        
#     count = 0    
#     if len(book) != 0:
#         for i in range(len(book)):
#             if book[i]["name"] == name:
#                 count+=1
#                 book[i]["scores"].append(scores)
#                 book[i]["average"] = sum(book[i]["scores"])/len(book[i]["scores"])
#         if count == 0:
#             average = max(scores)/len(scores)
#             dict2 ={
#             "name": name,
#             "scores": scores,
#             "average": average,
#            }
#             book.append(dict2)
#     return book    
# def get_average(book,name):
#     for items in book:
#         if items["names"] == name:
#             k = items["average"]
#     return k
# # def top_performer(book):
# #    ree 
    
    
# def remove_student(book,name):
#     count = 0
#     for i in range(len(book)):
#         if book[i]["name"] == name:
#             count+=1
#             del book[i]
#     return count == 1
# book = []
# add_student(book, "Soham", [88, 92, 79])
# add_student(book, "Riya", [95, 91])
# add_student(book, "Arjun", [72, 68, 80])
# add_student(book, "Soham", [95, 100])   # appends to Soham's scores

# print(get_average(book, "Soham"))        # (88+92+79+95+100)/5 = 90.8
# print(remove_student(book, "Arjun"))     # True
# print(remove_student(book, "Ghost")) 