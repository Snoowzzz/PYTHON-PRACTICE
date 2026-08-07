# # # f = open("Input\demo.txt","r")
# # # line1 = f.readline()
# # # line2 = f.readline()
# # # print(line1)
# # # print(line2)
# # # f.close()


# #writing a value then reading from the start using
# # seek function.... 

# # f1 = open("info.txt","+a")
# # data1 = f1.write("\n what up bitch!! ")
# # f1.seek(0)
# # data_1 = f1.read()
# # f2 = open("Input\demo.txt","+w")
# # data2 = f2.write("this is just a demo file nothing more trying to use this file ")
# # f2.seek(0)
# # data_2 = f2.read()
# # print(data_1)
# # print(data_2)
# # f1.close()
# # f2.close()

# # opening a empty file through code
# # f = open("Sample.txt","a")
# # f.close()

# # using the proper syntax(rewritng a file with first printing its original content)
# # with open("Input\demo.txt","r") as f:
# #     data1 = f.read()
# #     print(data1)
# # with open("Input\demo.txt","+w") as f:
# #     data2 = f.write("bakchodi on top bolte")
# #     f.seek(0)
# #     data2 = f.read()
# #     print(data2)
    
# #deleting a file
# import os
# # f = open("Sample.txt","+a")
# # data = f.write("Hello")
# # f.seek(0)
# # data = f.read()
# # print(data)
# os.remove("Sample.txt")

