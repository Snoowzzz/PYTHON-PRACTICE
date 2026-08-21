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
    
    
def updates_score(d,name,score):  
    if name not in d.keys():
      d[name] = score
    else:
        if d[name] < score:
            d.update({name:score})
    return d
d = {"Soham": 88, "Riya": 95}
news = updates_score(d, "Soham", 91)
print(news)
k = updates_score(d, "Soham", 100) 
t = updates_score(d, "Arjun", 72)
print(t)