# Exception
# difference type of Runtime exception and Exception
# Exception is a checked exception  

# IndexError


# marks = [45, 67, 89, 23]
# print(marks[5])  # IndexError: list index out of range
# # Runtime exception is an unchecked exception
# print(10 / 0)  # ZeroDivisionError: division by zero
# checked exception is an exception that is checked at compile time.
# unchecked exception is an exception that is not checked at compile time.
# checked exception is also known as compile-time exception.
# unchecked exception is also known as runtime exception.
# checked exception is a subclass of Exception class.

# KeyError
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict['@'])  # KeyError: 'd'
# KeyError is an exception that is raised when a key is not found in a dictionary.
# KeyError is a subclass of LookupError class.
# LookupError is a subclass of Exception class.
# KeyError is an unchecked exception.

# type error
# print('10' + 10)  # TypeError: can only concatenate str (not "int") to str
# TypeError is an exception that is raised when an operation or function is applied to an object

# Execept Handler  =======>

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = (a+b)/2
# print("Average is: ", c)

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = (a+b)/2
#     print("Average is: ", c)
# except Exception as e:
#     print("Error is: ", e) #that is of an inappropriate type.
# TypeError is a subclass of Exception class.
# TypeError is an unchecked exception.

# Concept  of  chomprehension

# Comprehension in Python provides a concise way to create lists, sets, or dictionaries. It consists of brackets containing an expression followed by a for clause, and can also include optional if clauses to filter items.

# l1 = [1, 2, 3, 4, 5]
# for i in range(1,6):
#     l1.append  (i*2)
# print(l1)

# lambda

# def add(x, y):
#     return x + y
# x = add(5, 10)
# print(x)


# add1 = lambda x, y: x + y
# x1 = add1(5, 10)    

# print(x1)
# lambda is a small anonymous function
# lambda can take any number of arguments, but can only have one expression.
# lambda is a function that is defined without a name.
# lambda is also known as a lambda function or an anonymous function.
# lambda is a function that is defined using the lambda keyword.

# map function
# l1 = [1, 2, 3, 4, 5]    
# l2 = list(map(lambda x: x*2, l1)) # map function is used to apply a function to all the items in an iterable (list, tuple etc.)
# print(l2)
# map function is used to apply a function to all the items in an iterable (list, tuple etc.)
# map function returns a map object (an iterator) of the results after applying the given function
# map function is a built-in function in Python.
# map(function, iterable, ...)
# function: a function that is to be applied to each item of the iterable.  

# Applying a function to square numbers in a list
# numbers = [1, 2, 3, 4, 5]

# # Using a lambda function
# squared_numbers = map(lambda x: x**2, numbers)
# print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]

# # Using a predefined function
# def multiply_by_two(num):
#     return num * 2

# doubled_numbers = map(multiply_by_two, numbers)
# print(list(doubled_numbers)) # Output: [2, 4, 6, 8, 10]

# # Using map with multiple iterables
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# def add_numbers(a, b):
#     return a + b

# sum_lists = map(add_numbers, list1, list2)
# print(list(sum_lists)) # Output: [5, 7, 9]

# def attenance(attendance):
#     if attendance < 75:
#         return ("attens less than 75%")
#     elif attendance >= 75:
#         return ("attens more than 75%")
#     else:
#         return ("invalid input")
# # print(attenance(80))

# l1 = [70, 80, 90, 60, 50]
# for i in l1:
#     print(attenance(i))
# map(attenance, l1)
# print(list(map(attenance, l1)))

# # multiple iterables
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# def add_numbers(a, b):  # function that adds two numbers
#     return a + b    
# sum_lists = map(add_numbers, list1, list2) # map function that adds corresponding elements from two lists
# print(list(sum_lists)) # Output: [5, 7, 9]

# l2 = [10, 20, 30, 40, 50]
# l3 = [100, 200, 300, 400, 500]
# map (lambda x, y: x + y, l2, l3)
# print(list(map (lambda x, y: x + y, l2, l3)))


# filter function
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, l1)) # filter function is used to filter the items in an iterable (list, tuple etc.) based on a condition.
# print(even_numbers)


# def check(a):
 
#  vowels =[ 'a', 'e', 'i', 'o', 'u']
#  if a in vowels:
#      return True
#  else:
#         return False
#  print(check('b'))
# l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# vowel_list = list(filter(check, l1))        
