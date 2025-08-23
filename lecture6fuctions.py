# function and recursion
# function difination
# def calc_sum(a,b): #parameters
#     sum =a +b
#     print(sum)
#     return sum # return function
# calc_sum(4,7)

# @ avarrege of 3 numbers

# def calcu_ava (a, b , c ):
#     sum = a + b+ c
#     ava = sum/3
#     print(ava)
#     return ava
# calcu_ava(45,56,78)

# Recursion fucntion

# def show(n):
#     if (n == 0):  # base case for recursion stop .
#         return
#     print(n)
#     show(n-1)
# show(6)

# Recursion return

# def fact(n):
#     if (n==1  or n== 0 ):
#         return 1
#     return fact(n-1) *n
# print(fact(4))

# lets practics 
# Write a recursion fuction to calculate the sum of first n natural number

# def cal_sum(n):
#     if (n==0):
#         return 0 
#     return(n-1) +n

# sum=cal_sum(5)
# print( sum)

# print list 
# def print_list(list ,idx=0):
#     if (idx == len(list)):
#      return 
#     print(list[idx])
#     print_list(list, idx+1)

#     fruits = ["mango", "banana","date", "cherry"]
#     print_list(fruits)

# gg