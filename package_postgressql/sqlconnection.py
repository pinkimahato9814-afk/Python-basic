import psycopg2

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        host="localhost",
        database="ok_test3",
        user="postgres",
        password="easy",
        port="5432"
    )

    print(" Connected to PostgreSQL successfully!")

    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS employees (
         id INT PRIMARY KEY,
         name VARCHAR(100),
         salary FLOAT,
         age INT        
       )
    """)

    

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))
    age = int(input("Enter Age: "))

    cursor.execute(
            "INSERT INTO employees (id, name, salary, age) VALUES (%s, %s, %s, %s)",
            (emp_id, name, salary, age)
        )
    print(" Employee added successfully!")


    # cursor.execute(
    #     "DELETE FROM employees WHERE id = %s",
    #     (emp_id,)
    # )



    # Update employee name: ritu → pinki
    # cursor.execute(
    #     "UPDATE employees SET name = %s WHERE name = %s",
    #     ('pinki', 'ritu')
    # )

    # Commit the changes
    connection.commit()

    print(" Employee name updated successfully!")

except Exception as error:
    print("Error while connecting:", error)

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print(" Connection closed.")





# import psycopg2

# # -------------------------------
# # Database Connection
# # -------------------------------
# def get_connection():
#     return psycopg2.connect(
#         host="localhost",
#         database="ok_test3",
#         user="postgres",
#         password="easy",
#         port="5432"
#     )


# def create_table(cursor):
#     cursor.execute("""
# create table if not exists students(
                   
#                    id int primary key,
#                    name varchar(1000) NOT NULL,
#                    age int,
#                    email varchar(2000)
#                    )
                   
                   
#                    """)

# # -------------------------------
# # Add students
# # -------------------------------
# def add_students(cursor):
#     try:
#         id = int(input("Enter Employee ID: "))
#         name = input("Enter Employee Name: ")
#         age = float(input("Enter age: "))
#         email = int(input("Enter email: "))

#         cursor.execute(
#             "INSERT INTO employees (id, name, salary, age) VALUES (%s, %s, %s, %s)",
#             (id, name, age, email)
#         )
#         print(" students added successfully!")

#     except Exception as e:
#         print(" Error adding students:", e)

# # -------------------------------
# # view  students
# # -------------------------------

# def view_students(cursor):
#     cursor.execute("SELECT * FROM students ORDER BY id") #
#     records = cursor.fetchall()

#     if records:
#         print("\n--- students List ---")
#         for row in records:
#             print(f"ID: {row[0]}, Name: {row[1]}, age: {row[2]}, email: {row[3]}")
#     else:
#         print("No students found.")


# # -----------------------------
# # update students
# # -------------------------------

# def update_students(cursor):
#     new_id = int(input("Enter Employee ID to update: "))
#     new_name = input("Enter New Name: ")
#     new_age = float(input("Enter New age: "))
#     new_email = int(input("Enter New email: "))

#     cursor.execute(
#         "UPDATE employees SET name=%s, salary=%s, age=%s WHERE id=%s",
#         (new_name, new_age, new_email, new_id)
#     )

#     if cursor.rowcount > 0:
#         print(" Employee updated successfully!")
#     else:
#         print(" Employee not found.")



# # -------------------------------
# # Delete Employee
# # -------------------------------
# def delete_students(cursor):
#     id = int(input("Enter students ID to delete: "))
#     cursor.execute("DELETE FROM students WHERE id = %s", (id,))

#     if cursor.rowcount > 0:
#         print(" students deleted successfully!")
#     else:
#         print(" students not found.")






# # -------------------------------
# # Main Program
# # -------------------------------
# def main():
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         create_table(cursor)
#         connection.commit()

#         print(" Connected to PostgreSQL")
        
#         while True:
#             print("\n===== student Management System =====")
#             print("1. Add students")
#             print("2. View All students")
#             print("4. Update students")
#             print("5. Delete students")
#             print("6. Exit")

#             choice = input("Enter choice (1-6): ")

#             if choice == '1':
#                 add_students(cursor)
#                 connection.commit()
#             elif choice == '2':
#                 view_students(cursor)
#                 connection.commit()
#             elif choice == '4':
#                 update_students(cursor)
#                 connection.commit()
#             elif choice == '5':
#                 delete_students(cursor)
#                 connection.commit()
#             elif choice == '6':
#                 print("Exiting system...")
#                 break
#             else:
#                 print("Invalid choice. Try again.")

#     except Exception as error:
#         print("Database error:", error)

#     finally:
#         if 'connection' in locals():
#             cursor.close()
#             connection.close()
#             print(" Connection closed.")

# if __name__ == "__main__":
#     main()


