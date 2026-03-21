# # normal function
# def greet():
#     print("Hello Pinki")


# #create decurator
# def beautify(func):
#     def wrapper():
#         print("************")
#         func()
#         print("************")
#     return wrapper

# # use decurator
# @beautify
# def greet():
#     print("Hello Pinki")
    
# greet()
# # means decurator
# greet = beautify(greet)
# greet()

# #greet = beautify(greet)
# def beautify(func):
#     def wrapper(*args, **kwargs):
#         print("************")
#         func(*args, **kwargs)
#         print("************")
#     return wrapper

# @beautify
# def greet(name):
#     print("Hello", name)

# greet("Pinki")


# #Decorator With Return Value
# def beautify(func):
#     def wrapper(*args, **kwargs):
#         print("Starting...")
#         result = func(*args, **kwargs)
#         print("Finished!")
#         return result
#     return wrapper


# @beautify
# def add(a, b):
#     return a + b

# print(add(5, 3))


# def decurator(func):
#     print("before function calling")
#     func()
#     print("after function calling")
#     return func
# @decurator
# def greet():
#     print("Hello Pinki")

# purpose of using decurator is to modify the behaviour of function without changing its code
# 📌 Used for:

# Logging

# Printing messages

# Tracking execution time 
#this is decurator with return value

# def beautify(func1):
#     def wrapper(a,b):
#         print ("where are you goining")
#         result = func1(a,b)
#         print("where are you coming")
#         return result
#     return wrapper

# @beautify # this is decurated function
# def greet(a,b):
#     return a+b
# print(greet(5,6))



# def list_decurator(func):
#     def wrapper(*args,**kwargs):
#         print("list of arguement passed to functionis:")
#         print(args)
#         return func(*args,**kwargs)
#     return wrapper
# @list_decurator


# 🟢 Problem 2: Check Even Number
# 🎯 Task:

# Create a decorator that:

# Checks if the number passed to a function is even.

# If even → call the function

# If odd → print "Only even numbers allowed"

# Apply it to:

# def show_number(n):
#     print("Your number is:", n)

# Example:
# show_number(4) → allowed
# show_number(5) → not allowed

# def even_decurator(func):
#         def wrapper(n):
#             if n % 2 == 0:
#                 return func(n)
#             else:
#                 print("Only even numbers allowed")
#         return wrapper  
# @even_decurator
# def show_number(n):
#     print("Your number is:", n)
# show_number(7) # allowed
# show_number(12) # not allowed
   
# question is to create a decurator to check the execution time of function
# import time
# def decurator_time(func):
#     import time
#     def wrapper():
#         start_time = time.time()
#         print("first execution time:", start_time, "seconds")
#         func()
#         end_time = time.time()
#         print("second execution time:", end_time, "seconds")
#         print("total execution time:", end_time - start_time, "seconds")

#         return func()
#     return wrapper

# @decurator_time
# def show_function():
#     time.sleep(1)
#     return "function executed"
# show_function()



# 🟢 Problem 4: Modify Return Value
# 🎯 Task:

# Create a decorator that:

# Multiplies the result of a function by 10.

# Apply it to:

# def add(a, b):
#     return a + b

# Example:
# add(2,3)


# Expected result:

# 50   # (2+3)=5 → 

# def modify_return_value(func):
#     def wrapper(*args, **kwargs):
#         print("Modifying return value...")
#         result = func(*args, **kwargs)
#         modified_result = result * 10
#         print("modified return value:", modified_result)
#         #return modified_result
#     return wrapper

# @modify_return_value
# def add(a, b):
#     return a + b    
# add(2,3)

# define problem  number 5



# 🟢 Problem 5: Login Authentication System
# 🎯 Task:

# Create a decorator that:

# Checks if username == "admin"

# If yes → allow function execution

# If no → print "Access Denied"

# Apply it to:

# def dashboard(username):
#     print("Welcome to dashboard")

# def login_system(func):
#     def wrapper(username):
#         if username == "admin":
#             return func(username)
#         else:
#             print("Access Denied")
#     return wrapper  
# @login_system
# def dashboard(username):
#     print("Welcome to dashboard", username)
# username = input("Enter username:")
# dashboard(username)

 
# def loginsystem(func):
#         def wrapper(username,password):
#             if username == "admin" and password == "admin123":
#                 print("login successful")
#                 return func(username)
#             else:
#                 print("invalid name  or password ,denide access")    
#                 return None # do not call dashboard function if login fails
#         return wrapper  
# @loginsystem
# def dashboard(username):
#     print("Welcome to dashboard", username)
# username = input("Enter username:")
# password = input("Enter password:")

# dashboard(username,password)

import code


#we apply decurator to add function to modify its behaviour without changing its code
def beautify(func):
    def wrapper(a,b):
        print("where are you going")
        result = func(a,b)
        print("result is:", result)
        print("where are you coming")
        return result
    return wrapper

@beautify
def add(a, b):
    return a + b

result = add(5, 6)

