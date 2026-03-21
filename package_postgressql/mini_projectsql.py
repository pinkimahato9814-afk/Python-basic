import psycopg2

# -------------------------------
# Database Connection
# -------------------------------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ok_test3",
        user="postgres",
        password="easy",
        port="5432"
    )




# -------------------------------
# Create Table
# -------------------------------
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            salary FLOAT NOT NULL,
            age INT NOT NULL
        )
    """)

# -------------------------------
# Add Employee
# -------------------------------
def add_employee(cursor):
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        age = int(input("Enter Age: "))

        cursor.execute(
            "INSERT INTO employees (id, name, salary, age) VALUES (%s, %s, %s, %s)",
            (emp_id, name, salary, age)
        )
        print(" Employee added successfully!")

    except Exception as e:
        print(" Error adding employee:", e)

# -------------------------------
# View All Employees
# -------------------------------
def view_employees(cursor):
    cursor.execute("SELECT * FROM employees ORDER BY id")
    records = cursor.fetchall()

    if records:
        print("\n--- Employee List ---")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Salary: {row[2]}, Age: {row[3]}")
    else:
        print("No employees found.")

# -------------------------------
# Search Employee
# -------------------------------
def search_employee(cursor):
    emp_id = int(input("Enter Employee ID to search: "))
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    record = cursor.fetchone()

    if record:
        print("Employee Found:")
        print(f"ID: {record[0]}, Name: {record[1]}, Salary: {record[2]}, Age: {record[3]}")
    else:
        print(" Employee not found.")

# -------------------------------
# Update Employee
# -------------------------------
def update_employee(cursor):
    emp_id = int(input("Enter Employee ID to update: "))
    new_name = input("Enter New Name: ")
    new_salary = float(input("Enter New Salary: "))
    new_age = int(input("Enter New Age: "))

    cursor.execute(
        "UPDATE employees SET name=%s, salary=%s, age=%s WHERE id=%s",
        (new_name, new_salary, new_age, emp_id)
    )

    if cursor.rowcount > 0:
        print(" Employee updated successfully!")
    else:
        print(" Employee not found.")

# -------------------------------
# Delete Employee
# -------------------------------
def delete_employee(cursor):
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))

    if cursor.rowcount > 0:
        print(" Employee deleted successfully!")
    else:
        print(" Employee not found.")

# -------------------------------
# Main Program
# -------------------------------
def main():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        create_table(cursor)
        connection.commit()

        print(" Connected to PostgreSQL")
        
        while True:
            print("\n===== Employee Management System =====")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = input("Enter choice (1-6): ")

            if choice == '1':
                add_employee(cursor)
                connection.commit()
            elif choice == '2':
                view_employees(cursor)
            elif choice == '3':
                search_employee(cursor)
            elif choice == '4':
                update_employee(cursor)
                connection.commit()
            elif choice == '5':
                delete_employee(cursor)
                connection.commit()
            elif choice == '6':
                print("👋 Exiting system...")
                break
            else:
                print("Invalid choice. Try again.")

    except Exception as error:
        print("Database error:", error)

    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()
            print(" Connection closed.")

if __name__ == "__main__":
    main()