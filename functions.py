# Functions are integral to programming
    # Functional programming might not include OOP programming
    # You define functions and call them. That is it.

# Best practises
    # 1 function per function
    # you should only have one job per function to make it testable
    # your functions should return and not print (unless its really meant to print)
        # this is for reusability and testability

# functions help us keep our code dry
    # dont repeat yourself

# SYNTAX
    # def name(arg, arg2, arg3 = ''):
        #indent block of code

# The function needs to be called to run the block of code
# Call a function using its name and passing in parameters


def hello_person(f_name, l_name):
    result = 'Hello' + ' ' + f_name + ' ' + l_name
    return result

print(hello_person('Matt','Harding'))

