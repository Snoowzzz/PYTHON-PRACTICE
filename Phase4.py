### PHASE 4
# Q1 
# def describe(name,age,city):
#     return f"{name} is {age} years old and lives in {city}."
# print(describe("Soham",20,"Pune"))

# def list_stats(numbers):
#    new_lst = sorted(numbers)

#    def minimum():
#      return new_lst[0]

#    def maximum():
#      return new_lst[-1]

#    def average():
#       return sum(numbers) / len(numbers)

#    return minimum(), maximum(), round(average())


# numbers = [1, 2, 3, 4, 5]
# low, high, result = list_stats(numbers)
# print(low, high, result)

# The nested functions can only be called from inside list_stats(), because
# min, max, and avg are local names and are not available outside it.
# To call the function, pass a list as an argument:
#     list_stats([1, 2, 3, 4, 5])
# It returns (minimum, maximum, average).


## Q3