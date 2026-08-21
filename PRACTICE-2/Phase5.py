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

#### COULD NOT SOLVE IT THIS IS CLAUDES CORRECTED VERSION(logic was correct tho!!)
# def reversewords(words):
#     list1 = []
#     newstr = ""
#     i = 0
#     while i < len(words):
#         if words[i] == " ":
#             if newstr != "":        # only append if we built something
#                 list1.append(newstr)
#                 newstr = ""
#             i += 1
#         else:
#             newstr += words[i]      # build the word character by character
#             i += 1
#     if newstr != "":                # catch the last word
#         list1.append(newstr)
    
#     # now reverse the list
#     final = []
#     for i in range(len(list1)-1, -1, -1):
#         final.append(list1[i])
    
#     return " ".join(final)

# print(reversewords("Cloud Computing is fun"))   # fun is Computing Cloud
# print(reversewords("  hello   world  "))        # world hello
# print(reversewords("hello"))                    # hello

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
# def rotator(lst,t):
#     newlst = []
#     k = len(lst)
# #     for i in range(k):
# #         m = (i+t)%k
# #         newlst.insert(m,lst[i])

# #   slicing version (very short and precise)
# #   Derived on my own
#     p = t%k
#     newlst += lst[k-p:]
#     newlst += lst[0:k-p]
#     return newlst
# lst = [1,2,3,4,5] 
# t = 2
# newlst = rotator(lst,t)
# print(f"The Rotated list is: {newlst}")


## Q5 Medium (Tuples) ## Do not use dict
# Input:  "hello world"
# Output: [('l', 3), ('o', 2), ('d', 1), ('e', 1), ('h', 1), ('r', 1), ('w', 1)]

# def char_frequency(word):
#     list1 = []
#     word1 = word.replace(" ","")
#     for i in word1 :
#         ls = word1.count(i)
#         c = (i,ls)
#         list1.append(c)
#         c = ()
#     newlst = set(list1) 
#     newlst1 = sorted(newlst,key=lambda x: (-x[1], x[0]))
#     return newlst1    

# word = "hello world"
# newlst = char_frequency(word)
# print(f"Character count of the word: {newlst}")
# # Accessing a tuple through a list uses two indexes:
# list1[0]    -> ('l', 3), the first tuple in the list
# list1[0][0] -> 'l',    the string at index 0 of that tuple
# list1[0][1] -> 3,      the integer at index 1 of that tuple
# Indexing starts at 0: the first index selects the tuple, and the second
# index selects a value inside that tuple.
# print(list1[0][0])  # l
# print(list1[0][1])  # 3

# # Or unpack each tuple while looping through the list:
# for character, count in list1:
# 	print(character, count)
# sorted with key example
# pairs = [('b', 2), ('a', 3), ('c', 1)]
# # print(sorted(pairs,key=lambda x: (-x[1], x[0]))) 
# for i in pairs :
#   print(i[0],end=" ")
# # → [('c', 1), ('b', 2), ('a', 3)]  ascending

# # reverse it
# sorted(pairs, key=lambda x: x[1], reverse=True)
# # → [('a', 3), ('b', 2), ('c', 1)]  descending

### Q1 Hard string count (UPGRADED RLE) 

# Input:  "aaabbccddddef"
# Output: "3a2b2c4def"

# Input:  "abcd"
# Output: "abcd"   ← no counts since all are 1
# def stringcount(word):
#     i = 0
#     k = 0
#     count = 1
#     newstr = ""
#     for  i in range(len(word)-1):
#         k = i
#         if word[i] == word[i+1]:
#             count+=1
#             continue
#         if count>1:
#             newstr+= str(count)
#             newstr+= word[k]
#         else: 
#             newstr += word[k]
#         count = 1
#         k = 0
#    # Replace your second for loop with this:
#     if count > 1:
#         newstr += str(count)
#     newstr += word[-1]
#     return newstr
# word = "abcdddd"
# print(stringcount(word))

## Question 2 (Hard)

# print(row_sum(m, 1))    # → 15
# print(col_max(m, 2))    # → 9
# print(transpose(m))     # → [[1,4,7],[2,5,8],[3,6,9]]

def row_sum(m,k):
    sum = type(int)
    for i in range(len(m)):
        sum += m[i][k]
    return sum
def col_max(m,t):
    max = m[t][0]
    for i in range(len(m[t])):
        if m[t][i] >= max:
            max = m[t][i]
    return max
def transpose(m):
    list2 = []
    for i in range(len(m[0])):
        list1 =[]
        for j in range(len(m)):
            list1.append(m[j][i])
        list2.append(list1)
    return list2
            
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(row_sum(m, 0))
print(col_max(m, 1))
print(transpose(m))