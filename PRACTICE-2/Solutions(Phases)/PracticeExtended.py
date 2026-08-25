##### Extend pracitce for overall topics 
### Questions included in phase 6 questions
### Question 1 
# Input:  [3, 1, 4, 1, 5, 9, 2, 6]
# Output: [1, 3, 1, 4, 2, 9, 5, 6]  ← many valid answers exist
# def zigzag(lst):
#     lst.sort()
#     k = len(lst)
#     if len(lst) % 2 == 0:
#         lsta = lst[:int(k/2)]
#         lstb = lst[int(k/2) :]
#     else:
#         t = (k+1)/2
#         lsta = lst[:int(t)]
#         lstb = lst[int(t):]
#     finallst = []
#     for i in range(len(lstb)):
#         finallst.append(lsta[i])
#         finallst.append(lstb[i])
#     finallst.append(lsta[-1])
#     return finallst
# lst = [3, 1, 4, 1, 5, 9, 2]   
# print(zigzag(lst))    
        
### Question 2 (show index)
# Input:  ["the", "cat", "sat", "on", "the", "mat", "the"]
# Output: {"the": [0, 4, 6], "cat": [1], "sat": [2], "on": [3], "mat": [5]}
# def show_index(lst):
#     dct = {}
#     for i in range(len(lst)):
#         if lst[i] not in dct.keys():
#             dct[lst[i]]= []
#         dct[lst[i]].append(i)
#     return dct
# lst = ["the", "cat", "sat", "on", "the", "mat", "the"]
# print(show_index(lst))

# ### Question 3 (max_consecutives)
# Input:  [1, 1, 2, 2, 2, 1, 3, 3]
# Output: 3   ← three 2s in a row
# def max_consec(lst):
#     count = 1
#     countlst = []
#     for i in range(len(lst)-1):
#         if lst[i] == lst[i+1]:
#             count+=1
#             continue
#         countlst.append(count)
#         count = 1
#     countlst.sort()
#     return countlst[-1]
# lst = [1, 1, 2, 2, 2, 1, 3, 3]
# print(max_consec(lst))

#### Question 4
# Input:  [
#     {"name": "Soham", "city": "Pune"},
#     {"name": "Riya",  "city": "Mumbai"},
#     {"name": "Arjun", "city": "Pune"}
# ], key = "city"

# Output: {
#     "Pune":   [{"name": "Soham", ...}, {"name": "Arjun", ...}],
#     "Mumbai": [{"name": "Riya", ...}]
# }
# def bucket_data(lst,key):
#     finaldict = {}
#     for item in lst:
#         d = {}
#         for i,v in item.items():
#             if i == key:
#                 s = v
#                 continue
#             else:
#                 d[i] = v
#         if s not in finaldict.keys():
#             finaldict[s] = []
#         finaldict[s].append(d)
#     return finaldict            
            
# lst = [
#     {"name": "Soham", "city": "Pune","favourites":"Ambience Mall"},
#     {"name": "Riya",  "city": "Mumbai","favourites":"Marine Drive"},
#     {"name": "Arjun", "city": "Pune"}
# ]
# key = "city"
# print(bucket_data(lst,key))