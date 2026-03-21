# import psycopg2

# conn = psycopg2.connect(
#     host="localhost",
#     database="testdb",
#     user="postgres",
#     password="easy",
#     port="5432"
# )

# print("Connected successfully")

# conn.close()

# # -------------------------------
# # Create Table
# # -------------------------------
# def create_table(cursor):
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Departments(
#             id INT PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             type INT,
#             Address VARCHAR(200)
#         )
#     """)
# print("Table created successfully")

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="easy",
    port="5432"
)

print("Connected successfully")

cursor = conn.cursor()

# -------------------------------
# Create Table
# -------------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departments(
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        type INT,
        Address VARCHAR(200)
    )
""")

print("Table created successfully")

# -------------------------------
# Insert Data
# -------------------------------
cursor.execute("""
    INSERT INTO Departments (id, name, type, Address)
    VALUES (%s, %s, %s, %s)
""", (10, "Computer Science", 10001, "Kathmandu"))

conn.commit()

print("Data inserted successfully")

cursor.close()
conn.close()