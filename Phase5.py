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
        