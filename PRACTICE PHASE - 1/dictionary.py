# # Create a network access configuration map
# firewall = {
#     "HTTP": 80,
#     "HTTPS": 443,
#     "SSH": 22,
#     "PostgreSQL": 5432,
#     "info" : {
#     "name" : "Bakshi",
#     "marks" : 87,
#     "cgpa" : 9.1      
#     }
# }
# ssh_port = firewall["SSH"] 

# # 2. Production Standard Lookup: The .get() method
# # This prevents code crashes. If the protocol isn't found, it returns your default string.
# active_port = firewall.get("MySQL", "PORT_NOT_CONFIGURED")
# # print(f"The port for MYSQL is : ")
# # print(f"[SYSTEM] Secure SSH port allocation: {ssh_port}")
# # # print(firewall["HTTP"]) this can cause error if we print the wrong name
# # # print(firewall.get("HTTP")) no error simply return none if we enter the wrong value
# # print(list(firewall["info"]))

# #sets 
# collection = {"see this",5,"What is this",7,8,9,"This is adding",10}
# print(len(collection))
# collection.add("This is adding")
# collection.pop()
# collection.pop()
# print(collection)
# collection_1 = {4,5,7,8,9}
# set = collection.intersection(collection_1)
# print(set)
# student_info = {}
# for i in range(2):
#     name = input("Enter the name of the subject: ")
#     marks = int(input("Enter the marks you scored in that subject: "))
#     student_info[name] = marks
# print(student_info)
# print(bool(0))
# p,q,r = 0,2,3
# # print(p,q,r)
# my_dict = {
#     "name" :"Soham",
#      "age" : 17,
#      "hobbies" : ["Swimming","Dancing","Gaming"],
#      "personal_info" :{
#          "single": True,
#          "crush": "Many",
#          "gay": "No"
#      }
# }
# print(my_dict["personal_info"].keys())
