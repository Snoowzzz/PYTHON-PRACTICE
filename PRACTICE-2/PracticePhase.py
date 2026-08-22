# # ### Practice Dict

# # # def build_profile(name,age,city):
# # #     info = {
# # #         "name": name,
# # #         "age": age,
# # #         "city": city,
# # #     }
# # #     return info
# # # print(build_profile("Soham",21,"Pune"))

# # # dict = {
# # #     "name": "soham",
# # #      "age": 19,
# # #      "city": "Pune",
# # # }
# # # if "soham"  in dict.values():
# # #     print(True)
    
    
# # # def updates_score(d,name,score):  
# # #     if name not in d.keys():
# # #       d[name] = score
# # #     else:
# # #         if d[name] < score:
# # #             d.update({name:score})
# # #     return d
# # # d = {"Soham": 88, "Riya": 95}
# # # news = updates_score(d, "Soham", 91)
# # # print(news)
# # # k = updates_score(d, "Soham", 100) 
# # # t = updates_score(d, "Arjun", 72)
# # # print(t)


# # # ### Question 3
# # # Input:  "the cat sat on the mat the cat"
# # # Output: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}

# # # def word_count(sentence):
# # #     newstr = sentence.split(" ")
# # #     d = {}
# # #     for i in newstr:
# # #         if i not in d.keys():
# # #             k = newstr.count(i)
# # #             d[i] = k
# # #     return d
# # # sentence = "the cat sat on the mat the cat"
# # # k = word_count(sentence)
# # # print(k)

# # ## Question 4
# # def dict_flip(d):
# #     d1 = {}
# #     for k,v in d.items():
# #         d1[v] = k
# #     return d1
# # d =  {"a": 1, "b": 2, "c": 3}
# # print(dict_flip(d))

# ### Question 5
# def unique_names(lst):
#     setlst = set(lst)
#     return setlst
# def com_elems(lst1,lst2):
#     newset = set(lst1) & set(lst2)
#     return newset

# new =unique_names([1,2,2,3,3,3])    
# new1 =com_elems([1,2,3], [2,3,4])  
# print(new,"\n",new1)

### Question 6
# def set_elems(a,b):
#     s1 = set(a) & set(b)
#     s2 = set(a) - set(b)
#     s3 = set(a) | set(b)
#     return s1,s2,s3
# a = [1,2,3,4]
# b = [3,4,5,6]
# s1,s2,s3 = set_elems(a,b)
# print(f"Both: {s1}\nOnly in a: {s2}\nAll: {s3}")

# ### Tuples
# t = (1, 2, 2, 3)
# print(t.count(2))     # 2
# print(t.index(3))
# t1 = ([1, 2], 3)
# t1[0].append(99) 
# print(t1)  

## Question 7
# Input:  [3, 1, 4, 1, 5, 9, 2, 6]
# Output: (1, 9)
# def minimax(nums):
#     min = nums[0]
#     max = nums[0]
#     for i in nums:
#         if i >= max:
#             max = i
#         if i <= min:
#             min = i
#     return min,max

# nums =  [3, 1, 4, 1, 5, 9, 2, 6]
# min,max = minimax(nums)
# s= (min,max)
# print(s)   
   

# ## Question 8
# def swap_pairs(lst):
#     lst1 = []
#     for i,v in lst:
#         tupp = v,i
#         lst1.append(tupp)
#     return lst1
# lst = [(1,2), (3,4), (5,6)]
# swaplst = swap_pairs(lst)
# print(f"Swapped list: {swaplst}")

### Question 9
# list1 =  ["cat", "dog", "elephant", "ant", "ox", "bee"]
# print(len(list1[0]))
# Output: {3: ["cat", "dog", "ant", "bee"], 8: ["elephant"], 2: ["ox"]}
def groupby_length(words):
    d = {}
    for word in words:
        k = len(word)
        if k not in d:
            d[k] = []        # first time seeing this length, create empty list
        d[k].append(word)    # add word to that length's list
    return d
