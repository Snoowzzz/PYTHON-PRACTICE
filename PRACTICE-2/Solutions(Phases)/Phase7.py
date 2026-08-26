### PHASE — OOP: Mixed with prior topics (step 1)
# Question 1
# Input:  songs = [("Blinding Lights", 3), ("Levitating", 4), ("Peaches", 3)]
# Output: total_duration() -> 10

# class Playlist:
#     def __init__(self,songs): 
#         self.songs = songs
#     def total_duration(self):
#         sum = 0
#         for items in self.songs:
#             i,v = items
#             sum+=v
#         return sum
# songs = [("attention",168),("Catch me",140),("Shape of you",204)]
# s1 = Playlist(songs)
# print(s1.total_duration())

### Question 2 
# Input:  add_item("apple", 5); add_item("banana", 2); add_item("apple", 3)
# Output: self.stock -> {"apple": 8, "banana": 2}
#         total_items() -> 10

# class Inventory:
#     def __init__(self):
#         stock = {}
#         self.stock = stock
#     def add_item(self,name,quantity):
#         if name not in self.stock.keys():
#             self.stock[name] = quantity
#         else:
#             self.stock[name] += quantity
#     def show_items(self):
#         return self.stock
#     def total_items(self):
#         total_items = 0
#         for v in self.stock.values():
#             total_items += v
#         return total_items
# s1 = Inventory()
# s1.add_item("apple", 5)
# s1.add_item("banana", 2)
# s1.add_item("apple", 3)
# print(f"Stock: {s1.show_items()}\nTotal Items: {s1.total_items()}")

### Question 3
# Input:  text = "Hello World this is Python"
# Output: word_count() -> 5
#         shout() -> "HELLO WORLD THIS IS PYTHON"

# class Message:
#     def __init__(self,text):
#         count = 0
#         newstr = ""
#         for i in range(len(text)):
#             if text[i] == " ":
#                 count+=1
#                 continue
#             if count>0 and newstr != "":
#                 newstr += " "
#                 newstr += text[i]
#             else:
#                 newstr += text[i] 
#             count = 0   
#         self.text = newstr
#     def word_count(self):
        
#         newword = self.text.split(" ")
#         return len(newword)
#     def shout(self):
#         return self.text.upper()

# text = "   Hi   There   "  
# s1 = Message(text)          
# print(s1.word_count())
# print(s1.shout())
    

