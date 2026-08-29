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
#     if len(lst[a]) > len(lst)
#       finallst.append(lsta[-1])
#     return finallst

#######  CLEANER VERSION FOR THIS ############
# def zigzag(lst):
    # lst.sort()
    # k = len(lst)
    # mid = (k + 1) // 2
    # lsta, lstb = lst[:mid], lst[mid:]
    # finallst = []
    # for i in range(len(lstb)):
    #     finallst.append(lsta[i])
    #     finallst.append(lstb[i])
    # if len(lsta) > len(lstb):        # only true when k is odd
    #     finallst.append(lsta[-1])
    # return finallst
        
# lst = [3, 1, 4, 1, 5, 9, 2]   
# print(zigzag(lst))    
##--------------------------------------------------------------------------------------
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
##---------------------------------------------------------------------------------------------
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
#     countlst.append(count)
#     countlst.sort()
#     return countlst[-1]

# lst = [1, 1, 2, 2, 2, 1, 3, 3]
# print(max_consec(lst))
###-----------------------------------------------------------------------------------
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
#         count = 0
#         for i,v in item.items():
#             if key in item:
#                 count+=1
#                 if i == key:
#                     s = v
#                     continue
#                 else:
#                     d[i] = v
#         if count>0:
#             if s not in finaldict.keys():
#                 finaldict[s] = []
#             finaldict[s].append(d)
#     return finaldict  
          
# #### cleaner version 
# def bucket_data(lst, key):
#     finaldict = {}
#     for item in lst:
#         if key not in item:
#             continue          # decide: skip silently, or handle differently — see below
#         d = {}
#         for i, v in item.items():
#             if i == key:
#                 s = v
#             else:
#                 d[i] = v
#         finaldict.setdefault(s, []).append(d)
#     return finaldict        
# lst = [
#     {"name": "Soham", "city": "Pune","favourites":"Ambience Mall"},
#     {"name": "Riya",  "city": "Mumbai","favourites":"Marine Drive"},
#     {"name": "Arjun"}
# ]
# key = "city"
# print(bucket_data(lst,key))


#### Question 5
# Input:  "hello world"
# Output: {"h":[0], "e":[1], "l":[2,3,9], "o":[4,7], "w":[6], "r":[8], "d":[10]}
# def encode_pos(s):
#     d = {}
#     if len(s) == 0:
#         return d
#     for i in range(len(s)):
#         if s[i].islower() or s[i].isupper():
#             if s[i] not in d.keys():
#                 d[s[i]] = []
#             d[s[i]].append(i)
#     return d
# s ="hhhhhh12 hhhhhh"
# print(encode_pos(s))

#### Question 6

# pipeline([1, 2, 3, 4], [double, add_ten, keep_even])
# # double → [2,4,6,8]
# # add_ten → [12,14,16,18]
# # keep_even → [12,14,16,18]  ← all even here, but try other inputs
# Output: [12, 14, 16, 18]

# def triple(data):
#         return list(map(lambda x: x*3,data))
# def add_ten(data):
#         return list(map(lambda x: x+10,data))
# def keep_even(data):
#         return list(filter(lambda x: x%2 == 0,data))
# def pipeline(data,funcs):
#     for func in funcs:
#         k = func(data)
#         data = k
#     return k
# data =[1, 2, 3, 4]
# funcs =[triple, add_ten, keep_even]
# print(pipeline(data,funcs))

### Question 7 (smart_zip) not my logic i could not solve this one
# Input:  [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Output: [(1,4,6), (2,5,7), (3,None,8), (None,None,9)
# def smart_zip(lists):
#     if not lists:
#         return []
#     max_len = max(len(l) for l in lists)
#     result = []
#     for i in range(max_len):
#         row = tuple(l[i] if i < len(l) else None for l in lists)
#         result.append(row)
#     return result