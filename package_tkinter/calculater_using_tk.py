# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def multi(a,b):
#     return a * b

# def div(a,b):
#     return a / b

# def power(a,b):
#     return a ** b

# a = int(input("enter your number a :"))
# b = int(input("enter  your number b : "))
# operators = str(input("enter operator ( +, _ , * , /,**): "))
# if operators == "+":
#     print("result :" , add(a,b))
# elif operators == "-":
#          print("result :" , sub(a,b))
# elif operators == "*":
#       print("result :" , multi(a,b))   
# elif operators == "/":
#       print("result :" , div(a,b)) 
# elif operators == "**":
#       print("result :" , power(a,b))   
# else:
#       print("you invalid input")               



# import tkinter as tk

# def calculate():
#     try:
#         a = float(entry_a.get())
#         b = float(entry_b.get())
#         operator = operator_entry.get().strip()

#         if operator == "+":
#             result = a + b
#         elif operator == "-":
#             result = a - b
#         elif operator == "*":
#             result = a * b
#         elif operator == "/":
#             result = a / b
#         elif operator == "**":
#             result = a ** b
#         else:
#             result = "Invalid Operator"

#         result_label.config(text="Result : " + str(result))

#     except ValueError:
#         result_label.config(text="Enter valid numbers")
#     except ZeroDivisionError:
#         result_label.config(text="Cannot divide by zero")


# # Create window
# root = tk.Tk()
# root.title("Simple Calculator")
# root.geometry("350x250")

# # Labels and Entries
# tk.Label(root, text="Enter Number A").pack()
# entry_a = tk.Entry(root)
# entry_a.pack()

# tk.Label(root, text="Enter Number B").pack()
# entry_b = tk.Entry(root)
# entry_b.pack()

# tk.Label(root, text="Enter Operator (+, -, *, /, **)").pack()
# operator_entry = tk.Entry(root)
# operator_entry.pack()

# # Button
# tk.Button(root, text = "Calculate", command=calculate).pack(pady=10)

# # Result Label

# result_label = tk.Label(root, text="Result: ")
# result_label.pack()

# # Run App
# root.mainloop()


import tkinter as tk
from tkinter import messagebox

# Functions
def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operator = operator_var.get()

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = a / b
        elif operator == "**":
            result = a ** b
        else:
            messagebox.showerror("Error", "Invalid Operator")
            return

        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Enter number A").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Enter number B").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

# Operator selection
tk.Label(root, text="Select Operator").pack(pady=5)
operator_var = tk.StringVar()
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "**")
operator_menu.pack()

# Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=15)

# Result Label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()





