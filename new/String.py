# Strinng is a built-in data type in Python that represents a sequence of characters. Strings are immutable, meaning that once they are created, their content cannot be changed. They can be created using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) for multi-line strings.
# Strings can contain letters, numbers, symbols, and whitespace characters. They support various operations such as concatenation, slicing, and formatting. Python provides a rich set of string methods for manipulating and working with strings.
#         break # exit the loop


# a = "data analytics with python"
# print(a) # prints the string
# print(a.capitalize()) # Capitalizes the first letter of the string
# print(a.upper()) # Converts all characters to uppercase
# print(a.lower()) # Converts all characters to lowercase
# print(a.title()) # Capitalizes the first letter of each word
# print(a.swapcase()) # Swaps the case of each character
# print(a.count("a")) # Counts the occurrences of a substring in the string
# print(a.find("with")) # Finds the first occurrence of a substring and returns its index 
# print(a.replace("python", "java")) # Replaces occurrences of a substring with another substring
# print(a.split(" ")) # Splits the string into a list of substrings based on a delimiter
# print(a.strip()) # Removes leading and trailing whitespace characters
# print(len(a)) # Returns the length of the string
# print(a.index("analytics")) # Finds the first occurrence of a substring and returns its index (raises an error if not found)
# print(a.rindex("a")) # Finds the last occurrence of a substring and returns its index (raises an error if not found)
# print(a.slice(5)) # Slices the string from the specified start index to the end
# print(a.slice(5, 15)) # Slices the string from the specified start index


# Exmaple of for loop
# sum = 0
# for i in range(21): # range(start, stop, step)
#     sum += i # sum = sum + i
# print(sum)  # 210
# print(i)  # 0 2 4 6 8 10 12 14 16 18 20
# print(i)  # 0 2 4 6 8 10 12 14 16 18 20
# sum += i # sum = sum + i
# print(sum) # 110

# slining a string
# a = "Hello, World!"
# print(a[0]) # H - Accessing the first character
# print(a[7]) # W - Accessing the eighth character   
# print(a[-1]) # ! - Accessing the last character
# print(a[0:5]) # Hello - Slicing the first five characters
# print(a[7:]) # World! - Slicing from the eighth character to the end
# print(a[:5]) # Hello - Slicing the first five characters
# print(a[::2]) # Hlo ol! - Slicing with a step of 2
# print(a[::-1]) # !dlroW ,olleH - Reversing the string

# # Striping a string
# a = "   Hello, World!   "
# print(a.strip()) # "Hello, World!" - Removes leading and trailing whitespace
# print(a.lstrip()) # "Hello, World!   " - Removes leading whitespace
# print(a.rstrip()) # "   Hello, World!" - Removes trailing whitespace
# print(len(a)) # 21 - Length of the original string
# print(len(a.strip())) # 13 - Length after stripping whitespace
# print(a.replace(" ", "")) # "Hello,World!" - Removes all spaces by replacing them with an empty string


# # in build methods of string
# a = "data analytics with python"
# print(a) # prints the string
# print(a.capitalize()) # Capitalizes the first letter of the string
# print(a.upper()) # Converts all characters to uppercase 
# print(a.lower()) # Converts all characters to lowercase
# print(a.title()) # Capitalizes the first letter of each word
# print(a.swapcase()) # Swaps the case of each character
# print(a.count("a")) # Counts the occurrences of a substring in the string
# print(a.find("with")) # Finds the first occurrence of a substring and returns its index
# print(a.replace("python", "java")) # Replaces occurrences of a substring with another substring
# print(a.split(" ")) # Splits the string into a list of substrings based on a delimiter
# print(a.strip()) # Removes leading and trailing whitespace characters   
# print(len(a)) # Returns the length of the string
# print(a.index("analytics")) # Finds the first occurrence of a substring and returns its index (raises an error if not found)
# print(a.rindex("a")) # Finds the last occurrence of a substring and returns its index (raises an error if not found)
# print(a.slice(5)) # Slices the string from the specified start index to the end 
# print(a.slice(5, 15)) # Slices the string from the specified start index to the end


# # Looping in  strings
# a = "I am learning Python"
# for char in a: # iterate through each character in the string
#     print(char) # prints each character in a new line
# # count the number of vowels in a string
# vowels = "aeiouAEIOU"
# count = 0
# for char in a: # iterate through each character in the string
#     if char in vowels: # check if the character is a vowel
#         count += 1 # increment the count
# print("Number of vowels in the string:", count) # prints the count

# a = "I am learning Python"
# b = a.split(" ") # splits the string into a list of words
# for i in b: # iterate through each word in the list
#     print(i) # prints each word in a new line

# len = len(a)
# r  =  " "
# while len > 0:]
# r =r+ a[1-1]
# print(r) l= l-1
# print(r)

# Argument and Parmameders
# def add(a, b): # a and b are parameters

#     return a + b    
# result = add(5, 10) # 5 and 10 are arguments
# print(result) # 15
# result = add(20, 30) # 20 and 30 are arguments

# write a function to count the number of uppercase in a string

# def count_uppercase(s): # s is a parameter
#     count = 0 # initialization
#     for char in s: # iterate through each character in the string 
#         if char.isupper(): # check if the character is uppercase
#             count += 1 # increment the count
#     return count # return the count
# result = count_uppercase("Hello World") # "Hello World" is an argument
# print(result) # 2

# write a calculate_factorial(n): # n is a parameter    
# function to calculate the factorial of a number
