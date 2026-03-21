#import tkinter as tk

# # 1. Create root window
# root = tk.Tk()

# # #2. Set window title
# root.title("My First Tkinter App")


# # 3. Set window size
# root.geometry("400x300")  # width x height

# # 4. Run the main loop
# root.mainloop( )


import tkinter as tk

root = tk.Tk()

def say_hello():
    print("Hello")

label = tk.Label(root, text="Welcome")
label.grid(row=0, column=0, columnspan=3)

button1 = tk.Button(root, text="Login", command=say_hello)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="Register", command=say_hello)
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(root, text="Logout", command=say_hello)
button3.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()