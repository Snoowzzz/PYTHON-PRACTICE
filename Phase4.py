### PHASE 4
# Q1 
# def describe(name,age,city):
#     return f"{name} is {age} years old and lives in {city}."
# print(describe("Soham",20,"Pune"))

def list_stats():
   def min():
     return  new_lst[0]
   def max():
     return new_lst[-1]
   def avg():
      k = sum(list)/len(list)
      return k  
   low = min()
   high = max()
   result = avg()
list = [1,2,3,4,5]
new_lst = sorted(list)
print()

# The nested functions can only be called from inside list_stats(), because
# min, max, and avg are local names and are not available outside it.
# To call one, write min(), max(), or avg() inside list_stats().
# For example, you could call avg() after defining it:
#     result = avg()
#
# At the moment list_stats() does not call or return any of these functions,
# so calling list_stats(list) will not display a result.


