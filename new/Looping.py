# Looping Chapper 3
# Need of loop
# while Look
# print all the numbers from 0 to 10

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

#  print all the sum of 0 to 10
# i = 0  # initialization 
# sum = 0 # initialization
# while i <= 10: # condition
#     sum += i # sum = sum + i
#     i += 1 # increment
# print(sum)  # 55


# print all the even numbers from 0 to 10
# i = 0    # initialization
# while i <= 10:  # condition
#     if i % 2 == 0: # check if the number is even
#         print(i)
#     i += 1 # increment

# print all the odd numbers from 0 to 10
# i = 0    # initialization   
# while i <= 10:  # condition
#     if i % 2 != 0: # check if the number is odd
#         print(i)
#     i += 1 # increment

# For Loop
# for i in "Hello World":
#     print(i)


# word = "Hello World" # string
# for i in word: # iterate through each character in the string
#     print(i)       

# students = ["Alice", "Bob", "Charlie", "David"] # list
# for student in students: # iterate through each element in the list
#     print(student)

# i = 5
# for j in i: # range(start, stop, step)
#     print(j)  # 0 1 2 3 4   int is not iterable
# a = range(5) # range object
# for i in range(5): # range(start, stop, step)   
#     print(i)  # 0 1 2 3 4
# print(a) # range(0, 5)

# print all the numbers from 0 to 10
# for i in range(11): # range(start, stop, step)
#     print(i)  # 0 1 2 3 4 5 6 7 8 9 10
# # print all the even numbers from 0 to 10
# for i in range(0, 11, 2): # range(start, stop, step)
#     print(i)  # 0 2 4 6 8 10    
# # print all the odd numbers from 0 to 10
# for i in range(1, 11, 2): # range(start, stop, step)
#     print(i)  # 1 3 5 7 9
# # print all the numbers from 10 to 0
# for i in range(10, -1, -1): # range(start, stop, step)
#     print(i)  # 10 9 8 7 6 5 4 3 2 1 0  

# print all the sum of 0 to 20 using for loop
# sum = 0 # initialization
# for i in range(21): # range(start, stop, step)
#     sum += i # sum = sum + i
# print(sum) # 210


# print all the sum of even numbers from 0 to 20 using while loop
# sum = 0 # initialization
# for i in range(0, 21, 2): # range(start, stop, step)
#     sum += i # sum = sum + i   
# print(sum) # 110

# user_input = int(input("Enter a number: ")) # take input from user

# for i in range(1, 11): # range(start, stop, step)
#     print(f"{user_input} x {i} = {user_input * i}") # print multiplication table    
# # print multiplication table of user input number

# Playing with range 

# Fiboonacci series
# n = int(input("Enter the number of terms: ")) # take input from user
# a, b = 0, 1 # initialization
# count = 0 # initialization
# if n <= 0: # condition
#     print("Please enter a positive integer")
# elif n == 1: # condition    
#     print("Fibonacci sequence upto", n, ":")
#     print(a)

# a = 0
# b = 1
# for _ in range(1,11): # range(start, stop, step)
#     print(a) # print the first term
#     c= b  # update a to the next term
#     b = a + b # update b to the next term   
#     a = c # update a to the next term

# Break and Continue

# i = 0
# while i < 10: # condition
#     if i == 5: # condition
#         break # exit the loop
#     print(i) # print the value of i
#     i += 1 # increment

# example 
# find 20 odd numbers

# i = 0 # initialization
# counter = 0 # initialization
# while counter < 20: # condition
#     if i % 2 != 0: # check if the number is odd
#         print(i) # print the value of i
#         counter += 1 # increment the counter
#     i += 1 # increment the value of i

# prime number
# num = int(input("Enter a number: ")) # take input from user
# is_prime = True # initialization
# for i in range(2, num): # range(start, stop, step)
#     if num % i == 0: # check if the number is divisible by i
#         is_prime = False # set is_prime to False    
#         break
# if is_prime and num > 1: # check if the number is prime
#     print(f"{num} is a prime number") # print the result
# else:
#     print(f"{num} is not a prime number")
# # continue
# for i in range(10): # range(start, stop, step)
#     if i % 2 == 0: # check if the number is even
#         continue # skip the even numbers
#     print(i) # print the value of i


# i =0
# while i < 10: # condition
#     i += 1 # increment
#     if i  == 6: # check if the number is even
#         continue # skip the even numbers
#     print(i) # print the value of i

# a = "Data Analytics"
# for i in a :
#    if  i == "l":
#         continue
    
#    print(i)

# Nested Loops

# i = 0
# while i <= 4: # outer loop
#     j = 0
#     while j < 3: # inner loop
#      print(j, end=" ") # print the value of j
#      j += 1 # increment
#      i += 1

for i in range(5): # outer loop
    for j in range(3): # inner loop
        print(j, end=" ") # print the value of j
    print() # print a new line after each iteration of the