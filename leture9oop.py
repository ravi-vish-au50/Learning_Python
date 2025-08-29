# Del atribute (delete atribute)
# class Student :
#         def _init_ (self, name):
#             self.name = name

# s1= Student("Alice")
# print(s1.name)
# del s1.name
# print(s1)

# # Output: AttributeError: 'Student' object has no attribute 'name'
# # because we deleted the attribute name
# # If we try to access the deleted attribute, it will raise an AttributeError
# class account:
#     def __init__(self, acc_no, ac_pas): 
#        self.acc_no = acc_no
#        self.ac_pas = ac_pas
#        def reset_pas(self):
#           print(self.ac_pas)

# acc1 = account(12345, 'mypassword')
# print(acc1.acc_no)  # Output: 12345x    
# print(acc1.ac_pas)  # Output: mypassword
# print(acc1.reset_pas())  # Output: mypassword

# del acc1.ac_pas
# print(acc1.ac_pas)  # Output: AttributeError: 'account' object has no attribute 'ac_pas'
# # because we deleted the attribute ac_pas

class person:
   _name = "anonymous"

   def _hello(self):
    print("hello person")

def welcome(self):
       self._hello()
p1 = person()
print(p1._name)  # Output: anonymous

