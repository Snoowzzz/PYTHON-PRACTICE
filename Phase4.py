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


# ## Q1 Function to remove a negative from a list
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
#     for i in range(1,n+1):
#         new_lst.append(i**2)
#     return new_lst
# n = int(input("Enter the number till you want squares: "))
# new_lst = squares(n)
# if n>0:
#     print(f"Here is list of number which contains squares from 1 to {n}\n{new_lst}")
# else:
#     print(f"Enter a valid positive number..")


## Q4 return the index of first even number:
# def even_index(nums):
#     # enumerate(nums) is used here, so ch receives the index and i receives
#     # the corresponding value from nums.
#     for ch,i in enumerate(nums):
#         if i%2 == 0:
#             return ch
#     return -1
# nums = [4,5,6]
# print(even_index(nums))

# ## Q1 Medium ( modify a list remove duplicates from it without changing the order):
# def unique_ordered(nums):
#     new_list = []
#     for i in nums:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list        
# nums = [1,2,3]
# new_list = unique_ordered(nums)
# print(f"Modified List (without duplicates): {new_list}")


## Q2 Medium
# Input:  s = "abcdef", k = 2
# Output: "efabcd"
# def modify(s,t):
#     k = len(s)
#     char_lst = []
#     for i in range(k):
#         m = (i+t)%k
#         char_lst.insert(m,s[i])
#     final_str = "".join(char_lst)
#     return final_str
# s = input("Enter a string: ")
# t = int(input("By how much you want to  shift the string in Right: "))
# final_str = modify(s,t)
# print(f"Modified string: {final_str}")    


## Question 3 (Return the total grade count of the class)
# def getdict(list1):
#     dict1 = {
#       "A": 0,
#       "B": 0,
#       "C": 0,
#       "F": 0,  
#     }
#     for i in list1:
#         if  0<= i <=100:
#             if i >89:
#                 dict1["A"]+=1
#             elif 75<=i<90:
#                 dict1["B"]+=1
#             elif 50<= i <75:
#                 dict1["C"]+=1
#             else:
#                 dict1["F"]+=1  
#     return dict1
# list1 = [92,45,76,55,89,100,38]
# dict1 = getdict(list1)
# print(f"Following are the graded scores: \n{dict1}")            
            

# ## QUESTION 4 ( STRING  RECONSTRUCTOR)
# def consec_spaces(sentence):
#     k = len(sentence)
#     newstr = ""
#     count = 0
#     for i in range(k):
#         if sentence[i] == " ":
#             count+=1
#             continue
#         if count>0:
#             newstr+=" "
#             newstr+=sentence[i] ## this was the thing that i was missing for a long time
#         else:     
#             newstr += sentence[i]
#         count = 0
#     return newstr
# sentence = "CLoud    computing   is     fun   "
# newstr = consec_spaces(sentence)
# print(f"Your Modified String is {newstr}.")


## Hard Questions:
# Question 1
### H1 — List Flattener (Nested Lists)
# Input:  [1, [2, 3], 4, [5, 6, 7], 8]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# def flattener(data):
#     flat = [num for row in data for num in row]
#     return flat
# data = [1,[2,3],4, [5,6,7],8]
# flat = flattener(data)
# print(f"The simplified data is {data}")


def flattener(data):
    newdata = str(data).replace(",","").replace("[","").replace("]","").replace(" ","")
    flat_list = []
    for i in newdata:
        flat_list.append(int(i))
    return flat_list
        
data = [1, [2, [3, [4]]]]
flat_list = flattener(data)
print(f"Your Flattened List is: \n{flat_list}")

















