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
class Ledger:
    def __init__(self,owner):
        self.owner = owner
        self._transcation = []
    def credit(self,amount):
        if amount <= 0:
            raise ValueError("Enter a Valid amount")
        self._transcation.append(("credit",amount))
    def debit(self,amount):
        if amount <= 0:
            raise ValueError("Enter a Valid amount")
        self._transcation.append(("debit",amount))
    @property
    def balance(self):
        self.balance = 0
        for i,v in self._transcation:
            if i == "credit":
                self.balance += v
            elif i =="debit":
                self.balance -= v
        return self.balance
    def largest_credit(self):
        k = sorted(self._transcation,key=lambda x: (-x[1],x[0]))
        filterlst = list(filter(lambda x:  x[0] == "credit",k))
        if len(filterlst) == 0:
            return 0
        return filterlst[0][1]
    def summary(self):
        countcredit = 0
        countdebit = 0
        for i,v in self._transcation:
            if i == "credit":
                countcredit+=1
            elif i == "debit":
                countdebit+=1
        d = {
         "owner": self.owner,
         "credits": countcredit,
         "debits":  countdebit,
         "balance": self.balance,
        }
        return d
ledger = Ledger("Soham")
ledger.credit(500)
ledger.credit(200)
ledger.debit(100)
ledger.credit(800)
ledger.debit(300) 
print(ledger.balance)
print(ledger.largest_credit())      
print(ledger.summary())