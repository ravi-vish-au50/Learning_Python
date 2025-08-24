# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f= open("new.txt","a+") 
# data = f.write("abc")
# print(data)
# f.close()

# with open("demo.txt","r") as f :
#     data = f.read()
#     print(data)

# file detleting

# import os
# os.remove("demo.txt")

# lets practice

# with open("practice.txt","w") as f :
#     f.write("Hi everyone\nwe are learing file  I/O\n")
#     f.write("using java.\nI like programming in java.")
    # data = f.read()
    # if (data.find(word) != -1):
    #     print("FOUND")
    # else :
    #     print("not found")

# def check_for_line():
#     word = "learing"
#     data = True
# with open("practice.txt","r") as f :
#     while data :
#         data = f.readline()
#         if(word in data):
#         print(line_no)
#         return
#     line_no  += 1
# return -1
# print(check_for_line())


# count = 0
# with open("practice.txt","r") as f:
#      data= f.read()
#      print(data)
# nums = data.split(",")
# for val in nums:
#        if(int(val) % 2==0):
#                 count += 1
# print(count)

    #  num = ""
    #  for i in range(len(data)):
    #       if(data[i]==","):
    #            print(int(num))
    #            num =""
    #       else:
    #            num+= data[i]
   