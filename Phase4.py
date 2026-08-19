# ### PHASE 4
# # Q1 
# # def describe(name,age,city):
# #     return f"{name} is {age} years old and lives in {city}."
# # print(describe("Soham",20,"Pune"))

# # def list_stats(numbers):
# #    new_lst = sorted(numbers)

# #    def minimum():
# #      return new_lst[0]

# #    def maximum():
# #      return new_lst[-1]

# #    def average():
# #       return sum(numbers) / len(numbers)

# #    return minimum(), maximum(), round(average())


# # numbers = [1, 2, 3, 4, 5]
# # low, high, result = list_stats(numbers)
# # print(low, high, result)

# # The nested functions can only be called from inside list_stats(), because
# # min, max, and avg are local names and are not available outside it.
# # To call the function, pass a list as an argument:
# #     list_stats([1, 2, 3, 4, 5])
# # It returns (minimum, maximum, average).


# ## Q3 Function to remove a negative from a list
# def remove_negatives(nums, count=0):
# # nums is required; count starts at 0 when no second argument is supplied.
#    new_lst = []
#    for i in nums:
#        if i >= 0:
#            new_lst.append(i) 
#        else:
#            count+=1
#            pass
#    return new_lst, count 
  
# nums = [-1,-2,-3,-5]
# # Calling without count makes count use its default value, 0.
# new_nums, count = remove_negatives(nums)
# # Unpack the returned tuple into new_nums and count.
# if count != len(nums):
#     print(new_nums, count)
# else:
#     print(f"There are no positive numbers in the list: {new_nums}")


## Q2 (Easy one return the count of vowels in a string)
# def count_vowels(word,count=0):
#     new_word = word.lower()
#     vowels = ["a","e","i","o","u"]
#     for i in new_word:
#         if i in vowels:
#             count+=1
#     return new_word,count
# word = input("Enter anything: ")
# new_word,count = count_vowels(word)
# if count == 0:
#     print(f"There are no vowels in the word:  {word}")
# else:
#     print(f"Vowels in {word}: {count}")

# ## Q3
# def squares(n):
#     new_lst = []
#     for i in range(n):
#         k = (i+1)**2
#         new_lst.append(k)
#     return new_lst
# n = int(input("Enter the number till you want squares: "))
# new_lst = squares(n)
# if n>0:
#     print(f"Here is list of number which contains squares from 1 to {n}\n{new_lst}")
# else:
#     print(f"Enter a valid positive number..")
