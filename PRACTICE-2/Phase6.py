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
# #     for i in a:
# #         if i not in b:
# #             newlst.append(i)
# #     return newlst
# # a = [1, 1, 3, 4]
# # b = [1]
# # print(list_diff(a,b))

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
#     else:
#         count = 0
#         for i in range(len(book)):
#             if book[i]["name"] == name:
#                 count+=1
#                 for k in range(len(scores)):
#                     book[i]["scores"].append(scores[k])
#                 k = sum(book[i]["scores"])/len(book[i]["scores"])
#                 book[i]["average"] = k
#         if count == 0:
#             average = sum(scores)/len(scores)
#             dict2 ={
#             "name": name,
#             "scores": scores,
#             "average": average,
#            }
#             book.append(dict2)
            
# ### cleaner version of this
# ### suggested by claude (had thought of it)
# ### wanted to do first the simple way
#     # count = 0
#     # for i in range(len(book)):
#     #     if book[i]["name"] == name:
#     #         count += 1
#     #         for k in scores:
#     #             book[i]["scores"].append(k)
#     #         book[i]["average"] = sum(book[i]["scores"]) / len(book[i]["scores"])
#     # if count == 0:
#     #     book.append({
#     #         "name": name,
#     #         "scores": scores,
#     #         "average": sum(scores) / len(scores)
#     #     })

#     return book    
# def get_average(book,name):
#     count = 0
#     for items in book:
#         if items["name"] == name:
#             count+=1
#             k = items["average"]
#     if count> 0:
#         return k
#     else:
#         return False      
# def top_performer(book):
#     high = book[0]["average"]
#     list1 = []
#     for i in book:
#         if i["average"] >= high:
#             high = i["average"]
#     for i in book:
#         if i["average"] == high:
#             list1.append(i["name"])
#     if len(list1) > 1:
#         list2 = sorted(list1,key=lambda x: x.lower())
#         k = list2[0]
#     else:
#         k =list1[0]
#     return k
    
# def remove_student(book,name):
#     count = 0
#     for i in range(len(book)):
#         if book[i]["name"] == name:
#             k = i
#             count+=1
#     if count>0:
#         del book[k]
#         return True
#     else:
#         return False
# book = []
# add_student(book, "Soham", [88, 92, 79])
# add_student(book, "Riya", [95, 91])
# add_student(book, "Arjun", [72, 68, 80])
# add_student(book, "Soham", [95, 100])   # appends to Soham's scores

# print(get_average(book, "Soham"))        # (88+92+79+95+100)/5 = 90.8
# print(top_performer(book))
# print(remove_student(book, "Arjun"))     # True
# print(remove_student(book, "Ghost"))
# # book = [{"names":"soham","scores":[23,56,78],"average":sum()}] 
# # print(sum(book[0]["scores"]))


### Question 2 HARD (Recursion)
# Input:  "Cloud Computing is fun"
# Output: "fun is Computing Cloud"

# Rules:
# - Split on spaces is allowed
# - No loops — only recursion
# - Must handle single word and empty string

# def reverse_words_recursive(sentence):
#     newstr = ""
#     for i in range(len(sentence)):
#         if sentence[i].isalpha():
#             newstr += reverse_words_recursive(sentence[i+1:])
#         else:
#             newstr+=" "
#     return newstr
# sentence = "Cloud Computing is fun"
# print(reverse_words_recursive(sentence))

### Question 3 Hard (Super lengthy)
# Input: [
#     "soham:91", "RIYA:95", " arjun :72",
#     "soham:88",             # duplicate, keep 91
#     "meera:abc",            # invalid score, skip
#     ":45",                  # empty name, skip
#     "karan:38"
# ]

# Output: {
#     "roster":        [("Riya", 95), ("Soham", 91), ("Arjun", 72), ("Karan", 38)],
#     "class_average": 74.0,
#     "passed":        {"Riya", "Soham", "Arjun"},
#     "failed":        {"Karan"},
#     "highest":       ("Riya", 95)
# }
# def process_students(data):
#     lst = []
#     for items in data:
#         modstr = items.replace(" ","").split(":")
#         if len(modstr) == 2:
#             a = modstr[0]
#             b = modstr[1]
#             if a.isalpha() and b.isdigit():
#                 tupp = (a.capitalize(),int(b))
#                 lst.append(tupp)
### shifting to a dict to change values 
#     dct = {}
#     passed = set()
#     for items in lst:
#         i,v = items
#         if v>= 50:
#             passed.add(i)
#         if i not in dct.keys():
#             dct[i] = v
#         else:
#             if v > dct[i]:
#                 dct[i] = v
#### shifting to list because the output demands for it               
#     failed = set()
#     newlst = []
#     for i,v in dct.items():
#         if v < 50:
#             failed.add(i)
#         tupp = (i,v) 
#         newlst.append(tupp)     
#     avg = sum(dct.values()) / len(dct)
#     roster = sorted(newlst,key=lambda x: (-x[1],x[0]))
### Final nail in the coffin
#     cleandata = {
#         "roster": roster,
#         "class_average": avg,
#         "passed": passed,
#         "failed": failed,
#         "highest": roster[0]
#     }
#     return cleandata
    
# data = [
#     "soham:91", "RIYA:95", " arjun :72",
#     "soham:88",             # duplicate, keep 91
#     "meera:abc",            # invalid score, skip
#     ":45",                  # empty name, skip
#     "karan:38"
# ]
# print(process_students(data))


#### extended practice of phase 6 (questions added at the end
#### of phase 6 questions file
### Question 3
# Input:  nums = [1,1,1,2,2,3], k = 2
# Output: [(1, 3), (2, 2)]
# def num_count(nums,k):
#     lst = []
#     numlist = []
#     for i in nums:
#         if i not in numlist:
#             t = nums.count(i)
#             tupp = (i,str(t))
#             numlist.append(i)
#             lst.append(tupp)
#     return lst[:k]
# nums = [1,1,1,1,2,2,2,3,3,3,4,4] 
# k = 3
# print(num_count(nums,k))

## Question 4 (anagram)
# Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
def group_anagrams(words):
    lst = []
    d = {}
    for i in words:
       lst.append(i.lower())
    for items in lst:
        asciinum = []
        newstr = ""
        for i in items:
           a = ord(i)
           asciinum.append(a)
        newstr = "".join(asciinum.sort())
        if newstr not in d.keys():
           d[newstr] = []
        d[newstr].append(items)
    finallst = []
    for i,v in d.items():   
        finallst.append(v)
    return finallst   
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))       
            
        
        
## Question 5 (running_stats)
# Input:  [4, 2, 6, 1]
# Output: [(0, 4, 4.0), (1, 6, 3.0), (2, 12, 4.0), (3, 13, 3.25)]
# def running_stats(num):
#     lst = []
#     sum = 0
#     for i in range(len(num)):
#        sum += num[i]
#        tupp = (i,sum,sum/(i+1))
#        lst.append(tupp)  
#     return lst
# num = [4, 2, 6, 1]
# print(running_stats(num))

## Question 6 (active usernames)
# lst = [
#     {"username": "soham", "active": True},
#     {"username": "riya", "active": False},
#     {"username": "arjun", "active": True}
# ]
# activelst = list(map(lambda x: x["username"] ,filter(lambda x: x["active"] == True,lst)))
# print(activelst)