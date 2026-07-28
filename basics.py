# # # # # # # # #$just mastering the basics of python
# # # # # # # # # Patient_name = input("What is your name ")
# # # # # # # # # Patient_age = input("What is your age ")
# # # # # # # # # Patient_status_New = input("Are you a new patient ")
# # # # # # # # # print(f"The details of the patient are\n Name -{Patient_name}\n Age - {Patient_age}\n Status_new - {Patient_status_New} ")
# # # # # # # # birth_year = input("Plz enter your birth year: ")
# # # # # # # # age = 2026 - int(birth_year)
# # # # # # # # print(age)


# # # # # # # #CALCULATOR FUNCTION

# # # # # # # num_1 = int(input("Enter a number: "))
# # # # # # # num_2 = int(input("Enter a number: "))
# # # # # # # Operation = str(input("Enter the operation you would like to perform +,-,/,*: "))
# # # # # # # add = num_1 + num_2
# # # # # # # sub = num_1 - num_2
# # # # # # # mul = num_1*num_2
# # # # # # # div = num_1/num_2

# # # # # # # if Operation == "+":
# # # # # # #   print(add)
# # # # # # # elif Operation == "-":
# # # # # # #   print(sub)
# # # # # # # elif Operation == "/":
# # # # # # #     print(div)
# # # # # # # elif Operation == "*":
# # # # # # #     print(mul) 
# # # # # # # else :
# # # # # # #     print("Plz enter a valid response")
# # # # # # #indendation test 5
# # # # # # course = "python was first a very old language, then python became a boring language then python became a shiity langauge and then python became a erasable language"
# # # # # # print(course.replace("python","C++"))
# # # # # price = 7
# # # # # print( price > 10 or price <)

# # # # print("Welcome to Weight Converter")
# # # # weight = float(input("Enter your weight: "))
# # # # factor = str(input("Press K for Kgs and P for pounds: "))
# # # # if factor == "P" or "p":
# # # #     weight= weight*2.2
# # # # elif factor == "K" or "k":
# # # #     weight = weight/2.2
# # # # else :
# # # #  print("Plz enter a valid response")
# # # # print(f"Your weight in {factor} is {weight:.2f}")
# # # Design generator
# # # i = 1
# # # while i <= 5:
# # #     print(i * "*")
# # #     i = i+1
# # # while i <=10 :
# # #     k = 11-i
# # #     print(k * "*")
# # #     i = i+1

# # #list practice
# names = ["soham","bakshi","Ayan","prathamesh"]
# print(names[2:5])



                  #cgpa calculator
# def gradepoints(marks):
#     if 90 <= marks <= 100:
#         return 10
#     elif 80 <= marks < 90:
#         return 9
#     elif 70 <= marks < 80:
#         return 8
#     elif 60 <= marks < 70:
#         return 7
#     elif 50 <= marks < 60:
#         return 6
#     elif 0 <= marks < 50:
#         return 0
#     return 0

# print("Hello welcome to the CGPA calculator!! ")
# Subjects = int(input("Plz enter the no of subjects: "))
# sum = 0
# credit_count = 0
# for i in range(1,Subjects+1):
#     name = str(input("Plz enter the name of your subject: "))
#     marks = int(input("Plz enter your marks in the subject: "))
#     credits = int(input("Plz enter the no of credits in this subject: "))
#     total_credits = gradepoints(marks)*credits
#     credit_count = credit_count + credits
#     sum = sum + total_credits
#     if total_credits == 0:
#         print(f"Sorry you failed in {name} ")
#     else:
#         print(f"You have passed the subject")
#     i = i+1
# Grade_points = sum/credit_count
# if Grade_points >= 9:
#     print(f"You aced your test !\n You scored a solid {Grade_points:2f} ")
# elif Grade_points >= 8:
#     print(f"You did good. Your score is {Grade_points:2f}")
# elif Grade_points >= 7:
#     print(f"You did decent. Your score is {Grade_points:2f}")
# elif Grade_points >= 6:
#     print(f"You did average. Your score is {Grade_points:2f}")
# else :
#     print(f"You did BAD. Your score is {Grade_points:2f}")

# sum_5 = 0
# sum_3 = 0
# sum_15 =0
# count = 0
# for num in range(0,50):
#        if num%3 == 0 and num%5==0:
#           sum_15  += num
#        elif num%3 == 0 and num%5!= 0:
#           sum_3 = sum_3 +num
#        elif num%5 == 0 and num%3 != 0:
#            sum_5= sum_5 +num
#        else:
#           count+= num
# total = count + sum_3 +sum_5 +sum_15
# print("The sum of numbers from 1 to 50 are split in the following ways")
# print(f"The sum of numbers multiples of 3 is {sum_3}\n The sum of numbers multiples of 5 is {sum_5}\n The sum of numbers multiples of 15 is {sum_15}\n Therefore the total sum is {total}")


# prime number detector
# print("Welcome to Prime Detector")
# number = int(input("Enter your Number: "))
# count = 0
# for i in range(2,number):
#    if number% i==0:
#      count+= 1
# if count > 0 :
#    print("The following number is not Prime")
# else:
#    print("The following number is Prime")


# number = int(input("Enter Your Number: "))
# count = 1  
# for i in range(1,number+1):
#     count = count *i
# print(f"The factorial of {number} is {count}")


# def factorial(num):
#   count = 1
#   if num == 1 or num == 0:
#      return 1
#   else:
#    while num >=2:
#      count =count* num*(num-1)
#      num= num -2
#    return count
# number = int(input("Enter your number: "))
# print(f"The factorial of the {number} is {factorial(number)}")


# IP ADDRESS VERIFIER
IP = input("Enter your Ip address: ")
k = IP.split('.')
def IP_valid():
  if Type == 1:
      if int(k[0]) < 128:
        print(f"The class of IP {IP} is A ")
      elif int(k[0]) < 192:
        print(f"The class of IP {IP} is B ")
      elif int(k[0]) < 224:
        print(f"The class of IP {IP} is C ")
      else:
        print(f"The class of IP {IP} is D ")
  else:
      print("Thankyou for visiting")
count = 0
while count!= 4:
  for i in range(0,4): 
   if int(k[i]) in range(1,256):
    count+=1
  if count == 4:
    break
  if count!= 4:
   print("Please enter a Valid IP address")

print("Valid Ip address ")
Type = int(input("Would like to know the Type of IP: Press '1' for Yes and '0' for NO "))
IP_valid()
   
  