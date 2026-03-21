# magic method question...?
# list and dictionary refer to in pthon is jason
# import json

# def printer(number_of_times):
#     if number_of_times  ==0:
#         return
    
#     while number_of_times >0:
#         print(f"i am getting print {number_of_times}")
#         return printer(number_of_times-1) 
    
# printer(5)    


# def printer( number_of_times,people =[], meanage =[]):
#     meanage = 0
#     if number_of_times  ==0:
#         print(f"stopping the recursion {number_of_times}")
#         return people,meanage
    
#     while number_of_times >0:
#         print(f"i am getting print {number_of_times}")

#         return printer(number_of_times-1) 
    


    
# people ,meanage = printer(5,['sita','rita','gita'],[23,45,67])    
# def printer(number_of_times, people=[]):
   

#     if number_of_times == 0:
     
#         mean_age = sum(age for name,age in people) / len(people) #age for nam,i want to append in dictionary

#         print("\nStopping recursion.")
#         print("People entered:", people)
#         print("Mean age is:", mean_age)
#         return people, mean_age

#     print(f"\nEntry {number_of_times}")
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))

#     people.append((name, age))

#     return printer(number_of_times - 1, people)


# # 🔹 CALL THE FUNCTION by using  
# printer(3)




# while  number_of_times >0:
#     print(f"i am getting printed for {number_of_times}")
#     people.append({
#         'name' : input("enter your name")
#         "age" : int(input("enter your age"))
#     })
#     return printer(number_of_times-1,people)
# people,meanage =(5)
# print(people,meanage)


#def get_numeric_value():
    

# def printer(number_of_times, people=[]):


#     if number_of_times == 0:
#         # Calculate mean age
#         if len(people) == 0:
#             print("No data entered.")
#             return people, 0

#         mean_age = sum(person['age'] for person in people) / len(people)

#         print("\nStopping recursion")
#         print("People:", people)
#         print("Mean age:", mean_age)

#         return people, mean_age

#     print(f"\ni am getting printed for {number_of_times}")

#     people.append({
#         'name': input("Enter your name: "),
#         'age': int(input("Enter your age: "))
#     })

#     return printer(number_of_times - 1, people)


# # Call function
# printer(3)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1) 
    
# n = int(input("enter your number: "))    
# result = factorial(n)
# print("facterial of your given number: ",result)


# sum of natural number by using recursion 
# def sum_natural(n):
#     total = 0 
#     for i in range(n):
#          total += i
#     print(" sum of natural number :",total)    

# sum_natural(5)


# Sum of natural numbers using recursion

def sum_natural(n):
    if n < 0:
        return "Please provide a positive number"
    elif n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

num = int(input("Enter a number: "))
result = sum_natural(num)
print("Sum of natural numbers:", result)