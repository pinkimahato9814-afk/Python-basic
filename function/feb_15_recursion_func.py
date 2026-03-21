#Recursion is when a function calls itself to solve a smaller piece of the same problem.



# def fibonacci(n):
#     if n <= 0:
#         return 0
#         #print(fibonacci(0))  # Output: 0
#     elif n == 1:
#         return 1
#        # print(fibonacci(1))  # Output: 1    
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))  # Output: 55



# def fibonacci(n):
#     if n <= 1:      # Base case
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# for i in range(8):
#     print(fibonacci(i),end =",")



# by using Recursive Fibonacci function it is logically complex and it is not efficient because it does a lot of redundant calculations. For example, to calculate fibonacci(5), it calculates fibonacci(4) and fibonacci(3), but to calculate fibonacci(4), it also calculates fibonacci(3) and fibonacci(2), and so on. This leads to an exponential growth in the number of function calls, making it inefficient for larger values of n.
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# # Print first 8 Fibonacci numbers
# for i in range(8):
#     print(fib(i), end=",")


#how can use while loop for fibonacci series

# while True:
#     n = int(input("enter the value of n:"))
#     if n < 0:
#         print("Please enter a non-negative integer.")
#     elif n==0:
#         print("Fibonacci series: 0")
#         break
#     elif n==1:
#         print("Fibonacci series: 0, 1")
#         break
#     else:
#         def fib(n):
#             if n <= 1:
#                 return n
#             return fib(n-1)+fib(n-2)
#         for i in range(n):
#             print(fib(i), end=",")
     
#from unicodedata import name

# while True:
#     name = input("enter the name:")
#     if name == "pinki":
#         print("pinki is best friend")
#     else:       
#         print("pinki is not best friend")    
#     break
# for i in range(5):
#     factorial = 1
#     for j in range(1,i+1):
#         factorial *=j
# print(f"Factorial of {i} is {factorial}")



# i want to print fibonacci series
def fibonacci()

