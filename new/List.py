# list
# what is list in python
# list is a collection which is ordered and changeable. Allows duplicate members.
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print(type(my_list))
# print(len(my_list))
# print(my_list[0])
# print(my_list[-1])
# print(my_list[1:4])
# print(my_list[:3])
# print(my_list[2:])
# print(my_list[:])

# list constructor
# my_list = list((1, 2, 3, 4, 5))
# print(my_list)    
# print(type(my_list))

# indexing and iteration
# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# for item in my_list:
#    print(item)
# for index in range(len(my_list)):
#    print(my_list[index])  
# for index, item in enumerate(my_list):
#    print(index, item)
# while loop
# i = 0 
# while i < len(my_list):
#    print(my_list[i])
#    i += 1
# # list comprehension
# my_list = [x for x in range(10)]
# print(my_list)
# my_list = [x**2 for x in range(10)]
# print(my_list)
# my_list = [x for x in range(10) if x % 2 == 0]
# print(my_list) 

# list methods
# my_list = [1, 2, 3, 4, 5]  # original list
# my_list.append(6) # add 6 to the end of the list
# print(my_list)  # [1, 2, 3, 4, 5, 6]
# my_list.insert(0, 0) # insert 0 at index 0
# print(my_list) # [0, 1, 2, 3, 4, 5, 6]
# my_list.remove(3) # remove first occurrence of 3
# print(my_list) # [0, 1, 2, 4, 5, 6]
# my_list.pop() # remove and return last item
# print(my_list) # [0, 1, 2, 4, 5]
# my_list.pop(0)  # remove and return item at index 0
# print(my_list) # [1, 2, 4, 5]
# my_list.clear() # remove all items
# print(my_list) # []
# my_list = [1, 2, 3, 4, 5] # reset list
# print(my_list.index(3)) # index of first occurrence of 3
# print(my_list.count(3)) # count occurrences of 3
# my_list.sort() # sort list
# print(my_list) # [1, 2, 3, 4, 5]    
# my_list.reverse() # reverse list
# print(my_list) # [5, 4, 3, 2, 1] 
# my_list2 = my_list.copy() # copy list
# print(my_list) # [5, 4, 3, 2]
# my_list = [1, 2, 3, 4, 5] # reset list
# my_list.slice(0, 2) # remove first two elements
# print(my_list) # [4, 3]
# # my_list = [1, 2, 3, 4, 5] # reset list
# # my_list.extend([6, 7, 8]) # extend list by adding elements
# # print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]
# my_list = [1, 2, 3, 4, 5] # reset list
# my_list[1:4]
# print(my_list) # [1, 4, 5]