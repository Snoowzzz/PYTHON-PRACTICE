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
# # Output: {3: ["cat", "dog", "ant", "bee"], 8: ["elephant"], 2: ["ox"]}

# def groupby_length(words):
#     d = {}
#     for word in words:
#         k = len(word)
#         if k not in d:
#             d[k] = []        # first time seeing this length, create empty list
#         d[k].append(word)    # add word to that length's list
#     return d


### Question 10
# def analyse(data):
#     set1 = set()
#     sum = 0
#     high_score = data[0][1]
#     for i,v in data:
#         set1.add(v)
#         sum+=v
#         if v>= high_score:
#             high_score = v
#     for i,v in data:
#         if v==high_score:
#             high_name = i  
#     avg = round(sum/len(data),2)  
#     dict1 ={
#       "highest": high_name,
#       "unique_scores": set1,
#       "average": avg,
#     }    
#     return dict1
# data = [("Soham", 91), ("Riya", 95), ("Arjun", 102), ("Soham", 91)]
# dict1 = analyse(data)
# print(dict1)

### Question 1
# Input:  {"Soham": 91, "Riya": 45, "Arjun": 72, "Meera": 38}
# Output: {"Soham": 91, "Arjun": 72}
# def filter_passing(grades):
#     newdict = {}
#     for i,v in grades.items():
#         if v > 50:
#            newdict[i] = v
#     return newdict
# grades =  {"Soham": 91, "Riya": 45, "Arjun": 72, "Meera": 38}
# newgrades = filter_passing(grades)
# print(newgrades)

## Question 2
# batch1 = {"Soham", "Riya", "Arjun", "Meera"}
# batch2 = {"Soham", "Riya", "Karan"}
# Output: {"Arjun", "Meera"}
# def who_left(batch1,batch2):
#     batch3 = batch1 - batch2
#     return batch3
# batch1 = {"Soham", "Riya", "Arjun", "Meera"}
# batch2 = {"Soham", "Riya", "Karan"}
# wholeft = who_left(batch1,batch2)
# print(wholeft)

## Question 3  ( indepently figured out selection sort but there it was incomplete)
# list1 = [("Soham", 91), ("Riya", 95), ("Arjun", 72)]
# for i in range(len(list1)):
#   if "Soham" in list1[i]:
#     print(True)
# # Output: [("Riya", 95), ("Soham", 91), ("Arjun", 72)]
# def sort_by_score(data):
#     list1 = []
#     used_names = []
#     for i in range(len(data)):
#         max = 0
#         for j in range(len(data)):
#             if data[j][0] not in used_names:
#                 if data[j][1] >= max:
#                     max = data[j][1]
#         for i,v in data:
#             if v == max:
#               tupp = (i,v)
#               break
#         list1.append(tupp)
#         used_names.append(tupp[0])        
#     return list1
# data = [("Soham", 91), ("Riya", 95), ("Arjun", 72)]
# print(sort_by_score(data))

## Question 4(dict merger)
# d1 = {"a": 10, "b": 5, "c": 8}
# d2 = {"b": 12, "c": 3, "d": 7}
# Output: {"a": 10, "b": 12, "c": 8, "d": 7}

# def merge_dicts(d1,d2):
#     newdict = {}
#     for i,v in d1.items():
#         for j,t in d2.items():
#             if i == j:
#                 if v>=t:
#                     newdict[i] = v
#                 else:
#                     newdict[j] = t
#             else:
#                 newdict[i] = v
#                 newdict[j] = t
#     return newdict
# d1 = {"a": 10, "b": 5, "c": 8}
# d2 = {"b": 12, "c": 3, "d": 7}
# print(merge_dicts(d1,d2))
            
# def merge_dicts(d1, d2):
#     newdict = {}
#     for k, v in d1.items():
#         newdict[k] = v          # add everything from d1 first
#     for k, v in d2.items():
#         if k in newdict:
#             if v > newdict[k]:  # only update if d2 value is higher
#                 newdict[k] = v
#         else:
#             newdict[k] = v      # key only in d2, just add it
#     return newdict

## Question 5
# Input:  "hello world"
# Output: {"l": 3, "o": 2}   ← only chars with count > 1
def char_freq_count(word):
    seen = ""
    d = {}
    for i in word:
        if i.islower() or i.isupper():
            if i not in seen:
                p = word.count(i)
                seen+=i
                if p > 1:
                    d[i] = p
    return d
word = "hello world"
freq_count = char_freq_count(word)
print(freq_count)