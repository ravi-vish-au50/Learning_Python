# Conditional  module for handling conditional statements in a custom scripting language.
# if & indentaion based blocks
# a = int(input("Enter first number: ")
#         if a > 0:
#         print("Positive")
#         print("End of if block")
        
place = input("Enter your country: ")
a = int(input("Enter your age: "))
if place == "Denmark":
    if a >= 18:
        print("You can vote in Denmark.")
    else:
        print("You cannot vote in Denmark.")
elif place == "USA":
    if a >= 18:
        print("You can vote in the USA.")
    else:
        print("You cannot vote in the USA.")
else:
    print("Voting rules unknown for your country.")


    # nested if statements
    # if-elif-else ladder
    