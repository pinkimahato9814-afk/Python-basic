import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
connection = sqlite3.connect("pinki.db")

# Create a cursor object
cursor = connection.cursor()

# Create a table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER
# )
#""")
cursor.execute("""
CREATE TABLE IF not exists employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
)
               
               """)


emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_salary = float(input("Enter Employee Salary: "))
pname = input("enter  your name")
page = int(input("enter your age"))

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (pname, page ))
cursor.execute("INSERT INTO employees (id,name, salary) VALUES (?, ?, ?)", (emp_id,emp_name,emp_salary))

# Save changes
connection.commit()

# Fetch data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
connection.close()








