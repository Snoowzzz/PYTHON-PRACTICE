### SOLUTIONS FOR PHASE 8

### Question 1 (Easy)
# class Inventory:
#     def __init__(self):
#         stock = {}
#         self._stock = stock
#     def add(self,item,qty):
#         if item not in self._stock.keys():
#             self._stock[item] = qty
#         else:
#             self._stock[item]+=qty
#     def remove(self,item,qty):
#         if item not in self._stock.keys():
#             raise ValueError("item doesn't exist")
#         else:
#            k =  self._stock[item] 
#            if k - qty >= 0:
#                self._stock[item] = k -qty
#            else:
#                raise ValueError("insufficient stock")
#     @property
#     def total(self):
#         total_items = 0
#         for value in self._stock.values():
#             total_items += value
#         return total_items
# inv = Inventory()
# inv.add("apple", 10)
# inv.add("banana", 5)
# inv.add("apple", 3)
# inv.remove("banana", 2)
# print(inv.total)  
# print(inv._stock)             
# print(inv.remove("mango", 1))           


### Question 2 (Medium)
# class Ledger:
#     def __init__(self,owner):
#         self.owner = owner
#         self._transcation = []
#     def credit(self,amount):
#         if amount <= 0:
#             raise ValueError("Enter a Valid amount")
#         self._transcation.append(("credit",amount))
#     def debit(self,amount):
#         if amount <= 0:
#             raise ValueError("Enter a Valid amount")
#         self._transcation.append(("debit",amount))
#     @property
#     def balance(self):
#         total = 0
#         for i,v in self._transcation:
#             if i == "credit":
#                 total += v
#             elif i =="debit":
#                total -= v
#         return total
#     def largest_credit(self):
#         k = sorted(self._transcation,key=lambda x: (-x[1],x[0]))
#         filterlst = list(filter(lambda x:  x[0] == "credit",k))
#         if len(filterlst) == 0:
#             return 0
#         return filterlst[0][1]
#     def summary(self):
#         countcredit = 0
#         countdebit = 0
#         for i,v in self._transcation:
#             if i == "credit":
#                 countcredit+=1
#             elif i == "debit":
#                 countdebit+=1
#         d = {
#          "owner": self.owner,
#          "credits": countcredit,
#          "debits":  countdebit,
#          "balance": self.balance,
#         }
#         return d
# ledger = Ledger("Soham")
# ledger.credit(500)
# ledger.credit(200)
# ledger.debit(100)
# ledger.credit(800)
# ledger.debit(300) 
# print(ledger.balance)
# print(ledger.largest_credit())      
# print(ledger.summary())

# ### Question 3 (Medium)
# def build_leaderboards(results):
#     d = {}
#     for i,v in results:
#         if i not in d.keys():
#             d[i]= v
#         else:
#             d[i]+=v
#     lst = []
#     for i,v in d.items():
#         lst.append((i,v))
#     newlst = sorted(lst,key=lambda x: (-x[1],x[0]))
#     finalist = []
#     rank = 1
#     for idx, (k, s) in enumerate(newlst):  ### remember this
#         if idx > 0 and s < newlst[idx-1][1]:
#             rank = idx + 1   # only advance rank when score actually drops
#         finalist.append((rank, k, s))
# results = [
#     ("Alice", 300), ("Bob", 450), ("Alice", 200),
#     ("Charlie", 450), ("Dave", 100), ("Bob", 50)
# ]
# print(build_leaderboards(results))

### Question 4( Medium)
# text = "The Quick brown FOX jumped over the lazy DOG"
# banned = ["fox", "dog", "the"]
# sanitise(text, banned) →
# "[REMOVED] Quick brown [REMOVED] jumped over [REMOVED] lazy [REMOVED]"

# def sanitise(text,banned_words):
#     newtext = text.split(" ")
#     banned = set(banned_words)
#     finallst = []
#     for item in newtext:
#         if item.lower() not in banned:
#             finallst.append(item)
#         else:
#             finallst.append("[REMOVED]")
#     return " ".join(finallst)
# text = "The Quick brown FOX jumped over the lazy DOG"
# banned = ["fox", "dog", "the"]
# print(sanitise(text,banned))

### Question 5 (Medium)




### Question 6 (Medium)
# records = [
#     ("cloud", "aws", 3), ("cloud", "gcp", 1), ("cloud", "aws", 1),
#     ("lang", "python", 5), ("lang", "python", 2), ("cloud", "gcp", 4),
#     ("lang", "java", 3)
# ]
# group_by_category(records) →
# {
#   "cloud": {"aws": [1, 3], "gcp": [1, 4]},
#   "lang":  {"python": [2, 5], "java": [3]}
# }
# def group_by_dictionary(records):
#     d = {}
#     for c, s, v in records:
#         if c not in d:
#             d[c] = {}
#         if s not in d[c]:
#             d[c][s] = []
#         d[c][s].append(v)
#         d[c][s].sort()
#     return d

# records = [
#     ("cloud", "aws", 3), ("cloud", "gcp", 1), ("cloud", "aws", 1),
#     ("lang", "python", 5), ("lang", "python", 2), ("cloud", "gcp", 4),
#     ("lang", "java", 3)
# ]
# print(group_by_dictionary(records))

### Question 7 (Hard)

# class VotingBooth:
#     def __init__(self,candidates):
#         self.d = {}
#         self.candidates = candidates
#         for person in self.candidates:
#             self.d[person] = 0 
#     def cast_vote(self,candidate):
#         if candidate not in self.candidates:
#             raise ValueError("Unregistered Candidate!!")
#         self.d[candidate] += 1
        
#     def results(self):
#         lst = []
#         for person in self.candidates:
#             lst.append((person,self.d[person]))
#         newlst = sorted(lst,key=lambda x: (-x[1],x[0]))
#         return newlst
#     def winner(self):
#         k = self.results()
#         diff = 0 
#         for char, (i,v) in enumerate(k):
#             if char == 0:
#                 diff += v
#             elif char == 1:
#                 diff -= v
#         if diff == 0:
#             return "TIE" ### if all votes = 0 winner is a tie (and the first position)
#                          ### will go to the alphabetically ascending name
#         else:
#             return k[0][0]
#     @property
#     def total_votes(self):
#         votes = 0
#         k = self.results()   
#         for i,v in k:
#             votes += v
#         return votes
# booth = VotingBooth(["Alice", "Bob", "Charlie"])
# for candidate in ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]:
#     booth.cast_vote(candidate)
# print(booth.results())    
# print(booth.winner())
# booth.cast_vote("Bob")
# print(booth.winner())