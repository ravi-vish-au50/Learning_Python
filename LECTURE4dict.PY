# Dictinory in python

# Dict = {
#     "Name" : "Ravi",
#     "cgpa" : 7.5,
#     "makrs" : [76 , 73, 85],
# }
# print(Dict)

# Nested Dictinory

# studdent = {
#     "name" : "surabh",
#     "subject" :{
#         "math" : 76,
#         "chem" : 78,
#         "phy" : 79,
#     },
#     "status" : "pass"
# }
# print(studdent)

# Set in python
# collection = {1,2,4,5}
# print(collection)
# print(len(collection))

# collection = set()
# print(type(collection))

# Lets practics section
# dict = {
#     "table" : ["a peac of furnituer", "list of lotus"],
#     "cat" : "a small animal",
# }

# subject = {
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }
# print(subject)
# print(len(subject))

marks = {}

x = int(input("entr math:"))
marks.update({"math": x})

x = int(input("entr phy:"))
marks.update({"phy": x})

x = int(input("entr chem:"))
marks.update({"chem": x})

print(marks)