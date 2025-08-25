# class Student:
#     name = "John"

# s1 = Student()
# print(s1.name)

# s1.name = "Alice"
# print(s1.name)

# class Car:
#     color = "Red"

# c1 = Car()
# print(c1.color)

# def new_func():
#     class Student:
#        name = "Ravi"

#     r1 = Student()
#     print(r1.name)

# new_func()  

# class Student:

#     # default constructor   
#     def __init__(self): 
#        pass
#     # parameterized constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Constructor called")
# s1 = Student("John", 20)
# print(s1.name, s1.age)

# s2 = Student("Alice", 22)
# print(s2.name, s2.age)

# class Student:

#     # default constructor   
#     def __init__(self,name, marks ): 
       
#        self.name = name
#        self.marks = marks
#        print("Default Constructor called")

# def get_avg(self):
#     sum = 0
#     for val in self.marks:
#         sum += val
#         print("Average:", self.name, sum/3)
#         s1 = Student("John", [85, 90, 78])
#         get_avg(s1)

#         s1.name = "Alice"
#         get_avg(s1)

# class account:
#     def __init__(self,balance, account_no):
#         self.account_no = account_no    
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.balance}")
#     def display(self):
#         print(f"Account No: {self.account_no}, Balance: {self.balance}")
# a1 = account(1000, "123456")
# a1.display()
# a1.deposit(500)
# a1.withdraw(200)   
# a1.withdraw(2000)   
# a1.display()