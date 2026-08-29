### SOLUTIONS FOR PHASE 8
class Inventory:
    def __init__(self):
        stock = {}
        self._stock = stock
    def add(self,item,qty):
        if item not in self._stock.keys():
            self._stock[item] = qty
        else:
            self._stock[item]+=qty
    def remove(self,item,qty):
        if item not in self._stock.keys():
            raise ValueError("item doesn't exist")
        else:
           k =  self._stock[item] 
           if k - qty >= 0:
               self._stock[item] = k -qty
           else:
               raise ValueError("insufficient stock")
    @property
    def total(self):
        total_items = 0
        for value in self._stock.values():
            total_items += value
        return total_items
inv = Inventory()
inv.add("apple", 10)
inv.add("banana", 5)
inv.add("apple", 3)
inv.remove("banana", 2)
print(inv.total)  
print(inv._stock)             
print(inv.remove("mango", 1))           
    