### Starting today these questions are significanlty harder than any of the previous 
# ones.

## Q1 (Join two list)
# Input:  a = [1, 2, 3], b = [10, 20]
# Output: [1, 10, 2, 20, 3]
# def merge_lsts(a,b):
#     k = len(a)
#     t = len(b)
#     newlst = []
#     if k>t:
#         for i in range(t):
#             newlst.append(a[i])
#             newlst.append(b[i])
#         for i in range(t,k):
#             newlst.append(a[i])
#     elif k == t:
#         for i in range(t):
#             newlst.append(a[i])
#             newlst.append(b[i])
#     else:
#         for i in range(k):
#             newlst.append(a[i])
#             newlst.append(b[i])
#         for i in range(k,t):
#             newlst.append(b[i])            
#     return newlst
# a = [1]
# b = [10,20,30]
# newlst = merge_lsts(a,b)
# print(f"The Merged list is: {newlst}")


## Cleaner version  (Use of minimum function) really smart
# def merge_lsts(a, b):
#     newlst = []
#     min_len = min(len(a), len(b))
#     for i in range(min_len):
#         newlst.append(a[i])
#         newlst.append(b[i])
#     newlst += a[min_len:]
#     newlst += b[min_len:]
#     return newlst

## Q2 (Palindrone checker)
# Input:  "Race Car"    → True
# Input:  "Cloud"       → False
# Input:  "A man a plan a canal Panama"  → True

# def is_palindrone(word):
#     word1 = word.replace(" ","")
#     word2 = word1.lower()
#     newstr = ""
#     for i in range(len(word2)-1,-1,-1): ## dont forget the -1(IMP for the code to work)
#         newstr+=word2[i]  
        
#     # my idea
#     # if newstr == word2:
#     #     return True
#     # else:
#     #     return False
    
#     ## cleaner version to return
#     return newstr == word2

# word = "Cloud"
# print(is_palindrone(word))


### Q1 Medium (List return only max)
# # Input:  [3, 1, 4, 1, 5, 9, 2, 6]
# # Output: [3, 3, 4, 4, 5, 9, 9, 9] 

# def running_max(nums):
#     newlst = []
#     for i in range(len(nums)):
#         if i == 0:
#             newlst.append(nums[i])
#             continue
        
#         ## First try had some serious flaw 
#         # else:
#         #     # if nums[i-1]>=nums[i]:
#         #     #     newlst.append(nums[i-1])      
#         #     # else:
#         #     #     newlst.append(nums[i])
         
#         ## MY complete working version  
#         else:
#             k = len(newlst)
#             if nums[i] > newlst[k-1]:
#                 newlst.append(nums[i])
#             else:
#                 newlst.append(newlst[k-1])    

#         ### Claude's Cleaner version (good)
#         #else:  
#             if nums[i] > newlst[-1]:  ## very smooth REMEMBER THIS TRICK!!! ###
#                 newlst.append(nums[i])
#             else:
#                 newlst.append(newlst[-1])

#     return newlst        
# nums = [3,1,4,1,5,9,2,6] 
# print(running_max(nums))

# # Q2 Medium (reversing a sentence)  
# Input:  "Cloud Computing is fun"
# Output: "fun is Computing Cloud"
         
# def reversewords(words):
#     list1 = []
#     newstr = ""
#     for i in range(len(words)):
#         if words[i] == " ":
#             continue
#         else:
#             if i < len(words)-1:
#                 while words[i+1] != " ":
#                     newstr += words[i]
#                     i+=1
#                 newstr += words[i]
#                 list1.append(newstr)
#         newstr = ""
#     return list1
# words = "Cloud Computing is fun"
# print(reversewords(words))

# ## Q3 Medium (With this logic At par at LEETCODE MEDIUM)
# # Input:  lst = [1,2,3,4,5,6,7], size = 3
# # Output: [[1,2,3], [4,5,6], [7]]

# def chunksplit(lst,k):
#     s = len(lst)
#     list2 = []
#     for i in range(0,s,k):
#         list1 = []
#         if k+i < s:
#             for t in range(i,k+i):
#                 list1.append(lst[t]) 
#             list2.append(list1)          
#         else:
#             for t in range(i,s):
#                 list1.append(lst[t])
#             list2.append(list1)
#     return list2
# lst = [1,2,3,4]
# size = 2
# list2 = chunksplit(lst,size)
# print(f"The Chunked list is: {list2}")

## Q4 MEDIUM (list rotator)
# Input:  lst = [1,2,3,4,5], t = 2
# Output: [4,5,1,2,3]
def rotator(lst,t):
    newlst = []
    k = len(lst)
#     for i in range(k):
#         m = (i+t)%k
#         newlst.insert(m,lst[i])

#   slicing version (very short and precise)
#   Derived on my own
    p = t%k
    newlst += lst[k-p:]
    newlst += lst[0:k-p]
    return newlst
lst = [1,2,3,4,5] 
t = 2
newlst = rotator(lst,t)
print(f"The Rotated list is: {newlst}")