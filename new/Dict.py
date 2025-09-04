# Initializing module: Dict

# age = {
#     "Alice": 30,
#     "Bob": 25,
#     "Charlie": 35
# }
# print(age)
# print(type(age))
# print(len(age))
# print(age["Alice"])
# print(age.get("Bob"))
# print(age.keys())   


# Retrieve in dictonary
# print(age.values())
# print(age.items())
# print("Charlie" in age) 
# print("David" in age)
# print(age.get("David", "Not Found"))


# Nested dictionary
# person = {
#     "name": "Alice",
#     "age": 30,
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "state": "NY"
#     },
#     "hobbies": ["reading", "traveling", "swimming"]
# }
# print(person) # print the entire dictionary
# print(person["address"]["city"]) # print the city from the nested address dictionary
# print(person["hobbies"][1])     # print the second hobby from the hobbies list
# print(len(person["hobbies"])) # print the number of hobbies
# print(person["hobbies"][-1]) # print the last hobby
# print(person["hobbies"][:2]) # print the first two hobbies
# print(person["hobbies"][:]) # print all hobbies
# print(person["hobbies"][1:3]) # print hobbies from index 1 to 2
# print("traveling" in person["hobbies"])
# print("gaming" in person["hobbies"]) 

# looping through dictionary
# for key in person:
#     print(key, person[key])
# for key, value in person.items():
#     print(key, value)

# person = {
#         "Ravi": 24,
#         "Raju": 25,
#         "Rahul": 26
#     }
# print(person)
# person["Ravi"] = 27 # update value
# print(person)
# person["Rajesh"] = 28 # add new key-value pair
# print(person)
# del person["Raju"] # remove key-value pair
# print(person)
# person.pop("Rahul") # remove key-value pair
# print(person)
# person.clear() # remove all key-value pairs
# print(person)
# person = {
#         "Ravi": 24,
#         "Raju": 25,
#         "Rahul": 26
#     }
# print(person)
# person2 = person.copy() # copy dictionary
# print(person2)
# person3 = dict(person) # another way to copy dictionary
# print(person3)
# person.update({"Ravi": 30, "Rakesh": 29}) # update dictionary
# print(person)
# print(len(person)) # number of key-value pairs

# for i in person:
#     print(i, person[i])

# Methods in dictionary

# person = {
#         "Ravi": 24,
#         "Raju": 25,
#         "Rahul": 26
#     }
# person.get("Ravi") # get value for key "Ravi"
# print(person.get("Ravi"))

# # add items in dictionary
# person["Rakesh"] = 29 # add new key-value pair
# print(person)

# age.update({"Suresh": 32}) # add new key-value pair using update()
# print(age)
# person.clear() # remove all key-value pairs
# print(person)
# person.update({"Ravi": 30, "Rakesh": 29}) # update dictionary
# print(person)
# print(len(person)) # number of key-value pairs
# print(person.keys()) # get all keys


# n = int(input("Enter number of entries: "))  
# d = {} # empty dictionary

# for i in range(1, n+1):  # read n entries  
#     d[i]= i*i # store in dictionary 
# print(d)
# # print(d.keys())1

# write a program to map two lists into a dictionary
# Name = ['Alice', 'Bob', 'Charlie']
# Age = [25, 30, 35]
# my_dict = {}
# for i in range(len(Name)):
#     my_dict[Name[i]] = Age[i]
# print(my_dict)

# write a progran sort a dictionary by key
# my_dict = {'b': 2, 'a': 1, 'c': 3}
# sorted_dict = dict(sorted(my_dict.items()))  # sort by key 
# print(sorted_dict)  # Output: {'a': 1, 'b': 2, 'c': 

# write a program to the get the top 3 city by temperature from a dictionary
# city_temps = {
#     'New York': 85,
#     'Los Angeles': 90,
#     'Chicago': 80,
#     'Houston': 95,
#     'Phoenix': 100
# }
# sorted_temps = sorted(city_temps.items(), key=lambda x: x[1],
#                       reverse=True)  # sort by temperature in descending order
# top_3_cities = dict(sorted_temps[:3])  # get top 3 cities
# print(top_3_cities)  # Output: {'Phoenix': 100, 'Houston': 95, 'Los Angeles': 90} 3}


# usinng loops

# temp = {
#     "delhi": 40,
#     "mumbai": 35,
#     "chennai": 38,
#     "kolkata": 37
# }

# val = sorted(temp.values(), reverse=True) #
# print(val)

# for i in range(0,3):
#     for j in temp:
#         if val[i] == temp[j]:
#             print(j)    


# check how many times a word is there in a sentance
a = " a fear leads to anger and anger leads to hate"
b = a.split()
d5 = {}

for i in b :
    if d5.get(i) == None:
        d5[i] = 1
        elif















































