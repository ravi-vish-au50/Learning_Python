print("hello world")

# Union
# a = {1,2,3}
# b = {4,5,6}
# c = a & b
# c = a.intersection(b)
# e = b.intersection(a)
# c
# d = a. union(b)
# d = b|a
# d
# print(c)

# Difference
# a = {1,2,3}  # a = {1,2,3,4,5}
# b = {3,4,5}  # b = {3,4,5,6,7}
# c = a - b  #  c = {1,2}
# c = a.difference(b) #  c = {1,2}
# c   
# d = b - a # d = {4,5} 
# d = b.difference(a) # d = {4,5}
# d   
# print(c)
# print(d)

# Symmetric Difference
# a = {1,2,3}  # a = {1,2,3,4,5}
# b = {3,4,5}  # b = {3,4,5,6,7}
# c = a ^ b  #  c = {1,2,4,5}
# c = a.symmetric_difference(b) #  c = {1,2,4,5
# c   
# d = b ^ a # d = {1,2,4,5}
# d = b.symmetric_difference(a) # d = {1,2,4,5}
# d   
# print(c)
# print(d)

# other methods in set
# a = {1,2,3,4,5}  # a = {1,2,3,4,5}
# a.add(6) # adding single element
# print(a)
# a.update([7,8,9]) # adding multiple elements
# print(a) 
# a.remove(3) # if element not found it will raise error
# print(a)
# a.discard(10) # if element not found it will not raise error
# print(a)
# a.pop() # removes and returns an arbitrary element
# print(a)  
# a.clear() # removes all elements
# print(a)

# assignments
# Check wheather a  string is a palagram or not palagram is a sentence that contains every letter of the alphabet at 
# that quick brown fox jumps over the lazy dog
# a = "The quick brown fox jumps over the lazy dog"
# b = set(a)
# count = 0
# for i in b:
#     if i.isalpha():
#         count += 1
# print(b)


# exmple = "The quick brown fox jumps over the lazy dog"

# set1 = {1,2,3}
# set2 = {2,3,4}
# result = set1.intersection(set2)
# print(result)  # Output: {2, 3}

# # which oparator is used for intersection of two sets?
# set1.union(set2)
# print(set1)  # Output: {1, 2, 3, 4}
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# result = set1.difference(set2)
# print(result)  # Output: {1, 2}

