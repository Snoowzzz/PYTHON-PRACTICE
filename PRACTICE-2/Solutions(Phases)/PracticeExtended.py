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

### Question 3 