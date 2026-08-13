#This file is for practice of python OOP
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # using the two underscore to hide the attribute ( making it private)
    def reset_pass(self):
        print(self.__acc_pass)
    
        
s1 = Account("Abcd123&yh",8976436)
print("THE account name and password are:\n",s1.acc_no,"\n",s1.reset_pass())  #in 
#this we display account name and password but it does the actual password gets
#printed outside this and in the print statement we see acc name and NONE

        