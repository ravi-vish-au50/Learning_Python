# Miscllanceous Concepts in Python

# format I

# a = "we are learning {}"
# b = a.format("python")
# print(b)

# s = "{} is a {} company"
# p = s.format("TCS", "IT")
# print(p)

# s = "{Company_name} is a {Company_type} company"
# p = s.format(Company_name="TCS", Company_type="IT")
# print(p)

# Format II
# d ={
#     "apple": 100,
#     "google": 200,
#     "facebook": 300,
#     "netflix": 400
#  }
# for i in d:
#     print("{:<10}: {:<15}".format(i, d[i]))

# Errors
# Issue/probelms in program because of which program stop abruptly or give the wrong output

# * Types of Errors
# 1. Syntax Error
# 2. Logical Error
# 3. Runtime Error

# 1. Syntax Error
# a = 90
# print("Value of a is: ", a)
# # syntax error due to missing parenthesis in print statement
# print "Value of a is: ", a

# # 2. Logical Error
# a = 100
# b = 200   
# c = a - b  # logical error, should be a + b
# print("The sum of a and b is: ", c)

# # 3. Runtime Error
a = 100
b = 0
c = a / b  # runtime error, division by zero

