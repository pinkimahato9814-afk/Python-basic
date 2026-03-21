# #create simple dictionary
# #dict1 = {"name":"pinki","age":24,"city":"delhi"}
# #print(dict1.get("age"))
# #dict2 = {"address": "ktm"}
# #dict2["address"] = "pokhara"
# #print(dict2.setdefault("name", "not found name"))# name value chane because it is not present in the dict2 initially
# #print(dict2.setdefault("name", "rita"))# name value will not change because it is already present in the dict2

# #dict2.update(name = "not found name")
# #print(dict2)

# #dict2.update(name = "mira")
# #print(dict2)

# #from os import name


# #operations = {
#  #   "add": lambda a, b: a + b,
#  #   "sub": lambda a, b: a - b,
#   #  "mul": lambda a, b: a * b,
# #}

# #print(operations["add"](3, 4))  # 7
# #print(operations["mul"](5, 6))  # 30



# #nums = [1, 2, 3, 4]

# #squares = list(map(lambda x: x * x, nums))
# #print(squares)

# #dict1 = {"a": 1, "b": 2, "c": 3}

# #students = {
#  #   "student1": {"name": "Alice", "age": 20, "marks": 85},
#   #  "student2": {"name": "Bob", "age": 21, "marks": 90},
#    # "student3": {"name": "Charlie", "age": 22, "marks": 88}
# #}
# # get all inner dictionary
# #result = list(map(lambda x: x, students.values()))
# #print(result)

# #Fetch a specific value (example: only marks from each dictionary)
# #marks = list(map(lambda x: x["marks"], students.values()))
# #print(marks)
# #age =list(map(lambda x:x["age"], students.values()))
# #print(age)
# #name = list(map(lambda x:x["name"], students.values()))
# #print(name)
   

# #List_of_person =[ "pinki","rina","riju","kritishma","sirist"]

# #mod_lsit = [f"{person:}"{i} in List_of_person if a in i.lower()]
# #print(mod_list)


# salaries =(1,2) or tuple(1,2)
# #print(salaries)
# #print(type(()))

# #tuple unpacking
# #a,b= salaries
# #print(a,b)
# for item in salaries:
#     print(item)

# #tuple unpacking
# a,b=salaries
# print(a,b) 
# #type casting 
# salaries_list =list(salaries)
# print(salaries_list)


# dict()
# {}
# #list of tuple
# #list of dictionary
# list_of_tuples =[]
# list_Of_dict = {}

# for _ in range(5):
#     name =input("enter name")
#     name =input("enter address")
#     name =input("enter religion")
#     name =input("enter age ")
#     print("*"*50)

#     list_of_tuples.append(())

#     dam ={}
#     dam.update (name =name)
#     dam.setdefault("address",address)




# # set remove duplicated value
# num_set = {1,2,3,3,4}
# print(num_set)

# even_numbers = {2,4,8,10}
# odd_numbers ={0,1,3,5,7}
# print(even_numbers.union(odd_numbers))
# print(odd_numbers .intersection(even_numbers))
# print(odd_numbers .difference(even_numbers))
# print(odd_numbers .symmatry (even_numbers))


# frozan_set = frozanset(odd_numbers)
#lambda x:x+5

#exit()
#range is generator function



# question 1
# take five input from user and store it in a lis
# take five input from user and store it in a dictionary with key as name and value as age
# take five input from user and store it in a set
# v1 =[]
# v2 ={}
# v3 =set()
# for _ in range(2):
#     name =input("enter name")
#     age =int(input("enter age").strip()) # strip() is used to remove any leading or trailing whitespace from the input string, ensuring that the age value is clean and can be correctly converted to an integer.
#     address =input("enter address")
#     print("*"*50)

#     v1.append(name)
#     v2.update({"name":name,"age":age})
#     v3.add(address)

# print(v1)
#print(v2)
# print(v3)

#for i in v2:     
    # i want to print only key from the dictionary not value
  # print(i)


# function start from basic to advance level  
# it accep in put and accept output and it is reusable code block

# def func1():
#     print("this is function 1")

# func1()    


# def add(a,b):
#    return f"sum is: {a+b}"

# print(add(3,6))

# def stuents(firtname,midname,lastname):
#     return f"Name is {firtname} {midname} {lastname}"

# firstname = input("Enter firstname:\t")
# midname = input("Enter midname:\t")
# lastname = input("Enter lastname:\t")

# print(stuents(firstname,midname,lastname))


# def containate_namres(*args):
#     for  i in args:
#         print(i)


# containate_namres("pinki","rita","mira","sita")


# name =[]

# def fun1(*args):
#     for i in args:
#         name.append(i)
#     return name


# for _ in range(5):
#     name1 = input("Enter name:\t")
#     fun1(name1)

# fun1(name1)


        
# names = [input("Enter name:\t") for _ in range(5)]
# def concatinate_names():
#     return " ".join(names)
#names =["pini","rita","mira","sita"]
# print(concatinate_names(*names))



#kwargs
# dict1 ={}
# def student_info(first_name,mid_name,last_name,**kwargs):
#  print(first_name ,mid_name, last_name,kwargs) 
 
# list_of_students = []
# for item in range(5):
#  dict1 ={}
 

# student_info(first_name,mid_name,last_name, **dict1)    


# def beautify(func):
#         def wrapper(*args, **kwargs):
#             print("Before function call")
#             result = func(*args, **kwargs)
#             print("After function call")
#             return result
        
#         return wrapper
# @beautify   # this is the function decurator it means function in side function 

# def greet(name):
#     print(f"Hello, {name}!")
# greet("Alice,ramu,mesu ,sita=ram")
    
    
    
# time model
# import time
# import datetime
# from collections import Counter, defaultdict
# import time

# current_time = time.time()
# print(current_time)
# current_datetime = datetime.datetime.now()
# print(current_datetime)


from datetime import datetime
import time

# Start time
start_time = datetime.now()
print("Start Time:", datetime.now())

# Sleep for 5 seconds
#time.sleep(5)

# # End time
# end_time = datetime.now()
# print("Execution Complete Time:", end_time.now())

# # Total execution time
# difference = end_time - start_time
# print("Total Execution Time:", difference)



def ma_dec(para1 ,param2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator applied with parameters: {para1}, {para2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@ma_dec("Hello", "World")
def my_function():
    print("This is my function.")
    
#w3 resource
