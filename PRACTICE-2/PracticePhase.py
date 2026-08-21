### Practice Dict

# def build_profile(name,age,city):
#     info = {
#         "name": name,
#         "age": age,
#         "city": city,
#     }
#     return info
# print(build_profile("Soham",21,"Pune"))

# dict = {
#     "name": "soham",
#      "age": 19,
#      "city": "Pune",
# }
# if "soham"  in dict.values():
#     print(True)
    
    
# def updates_score(d,name,score):  
#     if name not in d.keys():
#       d[name] = score
#     else:
#         if d[name] < score:
#             d.update({name:score})
#     return d
# d = {"Soham": 88, "Riya": 95}
# news = updates_score(d, "Soham", 91)
# print(news)
# k = updates_score(d, "Soham", 100) 
# t = updates_score(d, "Arjun", 72)
# print(t)


# ### Question 3
# Input:  "the cat sat on the mat the cat"
# Output: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}

# def word_count(sentence):
#     newstr = sentence.split(" ")
#     d = {}
#     for i in newstr:
#         if i not in d.keys():
#             k = newstr.count(i)
#             d[i] = k
#     return d
# sentence = "the cat sat on the mat the cat"
# k = word_count(sentence)
# print(k)

## Question 4
def dict_flip(d):
    d1 = {}
    for k,v in d.items():
        d1[v] = k
    return d1
d =  {"a": 1, "b": 2, "c": 3}
print(dict_flip(d))