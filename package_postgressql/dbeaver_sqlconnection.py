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

# # -------------------------------
# # Create Table
# # -------------------------------
# def create_table(cursor):
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students(
#             id INT PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             age INT,
#             email VARCHAR(200)
#         )
#     """)

# # -------------------------------
# # Add Student
# # -------------------------------
# def add_student(cursor):
#     try:
#         id = int(input("Enter Student ID: "))
#         name = input("Enter Student Name: ")
#         age = int(input("Enter Age: "))
#         email = input("Enter Email: ")

#         cursor.execute(
#             "INSERT INTO students (id, name, age, email) VALUES (%s, %s, %s, %s)",
#             (id, name, age, email)
#         )

#         print("✅ Student added successfully!")

#     except Exception as e:
#         print("❌ Error adding student:", e)

# # -------------------------------
# # View Students
# # -------------------------------
# def view_students(cursor):
#     cursor.execute("SELECT * FROM students ORDER BY id")
#     records = cursor.fetchall()

#     if records:
#         print("\n--- Student List ---")
#         for row in records:
#             print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")
#     else:
#         print("No students found.")

# # -------------------------------
# # Update Student
# # -------------------------------
# def update_student(cursor):
#     id = int(input("Enter Student ID to update: "))
#     name = input("Enter New Name: ")
#     age = int(input("Enter New Age: "))
#     email = input("Enter New Email: ")

#     cursor.execute(
#         "UPDATE students SET name=%s, age=%s, email=%s WHERE id=%s",
#         (name, age, email, id)
#     )

#     if cursor.rowcount > 0:
#         print("✅ Student updated successfully!")
#     else:
#         print("❌ Student not found.")

# # -------------------------------
# # Delete Student
# # -------------------------------
# def delete_student(cursor):
#     id = int(input("Enter Student ID to delete: "))

#     cursor.execute("DELETE FROM students WHERE id=%s", (id,))

#     if cursor.rowcount > 0:
#         print("✅ Student deleted successfully!")
#     else:
#         print("❌ Student not found.")

# # -------------------------------
# # Main Program
# # -------------------------------
# def main():
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         create_table(cursor)
#         connection.commit()

#         print("✅ Connected to PostgreSQL")

#         while True:
#             print("\n===== Student Management System =====")
#             print("1. Add Student")
#             print("2. View Students")
#             print("3. Update Student")
#             print("4. Delete Student")
#             print("5. Exit")

#             choice = input("Enter choice (1-5): ")

#             if choice == '1':
#                 add_student(cursor)
#                 connection.commit()
#             elif choice == '2':
#                 view_students(cursor)
#             elif choice == '3':
#                 update_student(cursor)
#                 connection.commit()
#             elif choice == '4':
#                 delete_student(cursor)
#                 connection.commit()
#             elif choice == '5':
#                 print("👋 Exiting system...")
#                 break
#             else:
#                 print("Invalid choice. Try again.")

#     except Exception as error:
#         print("Database error:", error)

#     finally:
#         if 'connection' in locals():
#             cursor.close()
#             connection.close()
#             print("🔒 Connection closed.")

# if __name__ == "__main__":
#     main()

# # IN this code only add button is work properly
# import tkinter as tk
# from tkinter import messagebox, ttk
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

# # -------------------------------
# # Database Operations
# # -------------------------------
# def create_table():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students(
#             id INT PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             age INT,
#             email VARCHAR(200)
#         )
#     """)
#     conn.commit()
#     conn.close()

# def add_student():
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "INSERT INTO students (id, name, age, email) VALUES (%s, %s, %s, %s)",
#             (entry_id.get(), entry_name.get(), entry_age.get(), entry_email.get())
#         )

#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Success", "Student Added Successfully")
#         clear_fields()
#         view_students()

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def view_students():
#     for row in tree.get_children():
#         tree.delete(row)

#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM students ORDER BY id")
#     rows = cursor.fetchall()
#     conn.close()

#     for row in rows:
#         tree.insert("", tk.END, values=row)

# def update_student():
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("""
#             UPDATE students 
#             SET name=%s, age=%s, email=%s 
#             WHERE id=%s
#         """, (entry_name.get(), entry_age.get(), entry_email.get(), entry_id.get()))

#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Success", "Student Updated Successfully")
#         clear_fields()
#         view_students()

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def delete_student():
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("DELETE FROM students WHERE id=%s", (entry_id.get(),))
#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Success", "Student Deleted Successfully")
#         clear_fields()
#         view_students()

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def clear_fields():
#     entry_id.delete(0, tk.END)
#     entry_name.delete(0, tk.END)
#     entry_age.delete(0, tk.END)
#     entry_email.delete(0, tk.END)

# # -------------------------------
# # GUI Design
# # -------------------------------
# root = tk.Tk()
# root.title("Student Management System")
# root.geometry("750x500")
# root.configure(bg="lightblue")

# create_table()

# tk.Label(root, text="Student Management System", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

# frame = tk.Frame(root, bg="lightblue")
# frame.pack(pady=10)

# tk.Label(frame, text="ID", bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
# entry_id = tk.Entry(frame)
# entry_id.grid(row=0, column=1)

# tk.Label(frame, text="Name", bg="lightblue").grid(row=1, column=0, padx=5, pady=5)
# entry_name = tk.Entry(frame)
# entry_name.grid(row=1, column=1)

# tk.Label(frame, text="Age", bg="lightblue").grid(row=2, column=0, padx=5, pady=5)
# entry_age = tk.Entry(frame)
# entry_age.grid(row=2, column=1)

# tk.Label(frame, text="Email", bg="lightblue").grid(row=3, column=0, padx=5, pady=5)
# entry_email = tk.Entry(frame)
# entry_email.grid(row=3, column=1)

# button_frame = tk.Frame(root, bg="lightblue")
# button_frame.pack(pady=10)

# tk.Button(button_frame, text="Add", width=12, command=add_student).grid(row=0, column=0, padx=5)
# tk.Button(button_frame, text="Update", width=12, command=update_student).grid(row=0, column=1, padx=5)
# tk.Button(button_frame, text="Delete", width=12, command=delete_student).grid(row=0, column=2, padx=5)
# tk.Button(button_frame, text="View", width=12, command=view_students).grid(row=0, column=3, padx=5)

# # Table
# tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Email"), show="headings")
# tree.heading("ID", text="ID")
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")
# tree.heading("Email", text="Email")
# tree.pack(fill=tk.BOTH, expand=True, pady=10)

# view_students()

# root.mainloop()


# in this code add update delet button is work properly by the healp of select item


# import tkinter as tk
# from tkinter import messagebox, ttk
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

# # -------------------------------
# # Create Table
# # -------------------------------
# def create_table():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students(
#             id INT PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             age INT,
#             email VARCHAR(200)
#         )
#     """)
#     conn.commit()
#     conn.close()

# # -------------------------------
# # Add Student
# # -------------------------------
# def add_student():
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "INSERT INTO students (id, name, age, email) VALUES (%s, %s, %s, %s)",
#             (entry_id.get(), entry_name.get(), entry_age.get(), entry_email.get())
#         )

#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Success", "Student Added Successfully")
#         clear_fields()
#         view_students()

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# # -------------------------------
# # View Students
# # -------------------------------
# def view_students():
#     for row in tree.get_children():
#         tree.delete(row)

#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM students ORDER BY id")
#     rows = cursor.fetchall()
#     conn.close()

#     for row in rows:
#         tree.insert("", tk.END, values=row)

# # -------------------------------
# # Select Row (Auto Fill)
# # -------------------------------
# def select_record(event):
#     selected = tree.focus()
#     values = tree.item(selected, 'values')

#     if values:
#         clear_fields()
#         entry_id.insert(0, values[0])
#         entry_name.insert(0, values[1])
#         entry_age.insert(0, values[2])
#         entry_email.insert(0, values[3])

# # -------------------------------
# # Update Student
# # -------------------------------
# def update_student():
#     selected = tree.focus()
#     if not selected:
#         messagebox.showwarning("Warning", "Select a student first")
#         return

#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("""
#             UPDATE students
#             SET name=%s, age=%s, email=%s
#             WHERE id=%s
#         """, (entry_name.get(), entry_age.get(), entry_email.get(), entry_id.get()))

#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Success", "Student Updated Successfully")
#         clear_fields()
#         view_students()

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# # -------------------------------
# # Delete Student
# # -------------------------------
# def delete_student():
#     selected = tree.focus()
#     if not selected:
#         messagebox.showwarning("Warning", "Select a student first")
#         return

#     confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
#     if not confirm:
#         return

#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("DELETE FROM students WHERE id=%s", (entry_id.get(),))

#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Success", "Student Deleted Successfully")
#         clear_fields()
#         view_students()

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# # -------------------------------
# # Clear Fields
# # -------------------------------
# def clear_fields():
#     entry_id.delete(0, tk.END)
#     entry_name.delete(0, tk.END)
#     entry_age.delete(0, tk.END)
#     entry_email.delete(0, tk.END)

# # -------------------------------
# # GUI Design
# # -------------------------------
# root = tk.Tk()
# root.title("Student Management System")
# root.geometry("800x550")
# root.configure(bg="#b0d4e3")

# create_table()

# tk.Label(root, text="Student Management System",
#          font=("Arial", 20, "bold"),
#          bg="#b0d4e3").pack(pady=10)

# form_frame = tk.Frame(root, bg="#b0d4e3")
# form_frame.pack(pady=10)

# tk.Label(form_frame, text="ID", bg="#b0d4e3").grid(row=0, column=0, padx=5, pady=5)
# entry_id = tk.Entry(form_frame)
# entry_id.grid(row=0, column=1)

# tk.Label(form_frame, text="Name", bg="#b0d4e3").grid(row=1, column=0, padx=5, pady=5)
# entry_name = tk.Entry(form_frame)
# entry_name.grid(row=1, column=1)

# tk.Label(form_frame, text="Age", bg="#b0d4e3").grid(row=2, column=0, padx=5, pady=5)
# entry_age = tk.Entry(form_frame)
# entry_age.grid(row=2, column=1)

# tk.Label(form_frame, text="Email", bg="#b0d4e3").grid(row=3, column=0, padx=5, pady=5)
# entry_email = tk.Entry(form_frame)
# entry_email.grid(row=3, column=1)

# button_frame = tk.Frame(root, bg="#b0d4e3")
# button_frame.pack(pady=10)

# tk.Button(button_frame, text="Add", width=12, command=add_student).grid(row=0, column=0, padx=5)
# tk.Button(button_frame, text="Update", width=12, command=update_student).grid(row=0, column=1, padx=5)
# tk.Button(button_frame, text="Delete", width=12, command=delete_student).grid(row=0, column=2, padx=5)
# tk.Button(button_frame, text="View", width=12, command=view_students).grid(row=0, column=3, padx=5)
# tk.Button(button_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=4, padx=5)

# # Table
# tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Email"), show="headings")
# tree.heading("ID", text="ID")
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")
# tree.heading("Email", text="Email")

# tree.pack(fill=tk.BOTH, expand=True, pady=10)

# tree.bind("<ButtonRelease-1>", select_record)

# view_students()

# root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# -------------------------------
# DATABASE CONNECTION
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
# GLOBAL VARIABLES
# -------------------------------
current_page = 1
records_per_page = 10

# -------------------------------
# CREATE TABLE
# -------------------------------
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(200)
        )
    """)
    conn.commit()
    conn.close()

# -------------------------------
# FETCH DATA WITH PAGINATION
# -------------------------------
def view_students():
    global current_page

    for row in tree.get_children():
        tree.delete(row)

    offset = (current_page - 1) * records_per_page
    search_text = search_entry.get()

    conn = get_connection()
    cursor = conn.cursor()

    if search_text:
        cursor.execute("""
            SELECT * FROM students
            WHERE name ILIKE %s
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (f"%{search_text}%", records_per_page, offset))
    else:
        cursor.execute("""
            SELECT * FROM students
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (records_per_page, offset))

    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

    page_label.config(text=f"Page {current_page}")

# -------------------------------
# NEXT / PREVIOUS
# -------------------------------
def next_page():
    global current_page
    current_page += 1
    view_students()

def previous_page():
    global current_page
    if current_page > 1:
        current_page -= 1
        view_students()

# -------------------------------
# ADD STUDENT
# -------------------------------
def add_student():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students VALUES (%s,%s,%s,%s)",
            (entry_id.get(), entry_name.get(),
             entry_age.get(), entry_email.get())
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student Added")
        clear_fields()
        view_students()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# UPDATE
# -------------------------------
def update_student():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE students
            SET name=%s, age=%s, email=%s
            WHERE id=%s
        """, (entry_name.get(),
              entry_age.get(),
              entry_email.get(),
              entry_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student Updated")
        view_students()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# DELETE
# -------------------------------
def delete_student():
    if not messagebox.askyesno("Confirm", "Delete this student?"):
        return
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s",
                       (entry_id.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student Deleted")
        clear_fields()
        view_students()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# AUTO FILL
# -------------------------------
def select_row(event):
    selected = tree.focus()
    values = tree.item(selected, "values")
    if values:
        clear_fields()
        entry_id.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_age.insert(0, values[2])
        entry_email.insert(0, values[3])

# -------------------------------
# CLEAR
# -------------------------------
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# -------------------------------
# GUI
# -------------------------------
root = tk.Tk()
root.title("Professional Student Admin Panel")
root.geometry("950x600")
root.configure(bg="#f4f6f9")

create_table()

# Header
tk.Label(root, text="Student Admin Dashboard",
         font=("Arial", 22, "bold"),
         bg="#f4f6f9").pack(pady=15)

# Search Bar
search_frame = tk.Frame(root, bg="#f4f6f9")
search_frame.pack()

tk.Label(search_frame, text="Search Name:",
         bg="#f4f6f9").pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(search_frame, text="Search",
          command=view_students).pack(side=tk.LEFT)

# Form
form_frame = tk.Frame(root, bg="#f4f6f9")
form_frame.pack(pady=10)

labels = ["ID", "Name", "Age", "Email"]
entries = []

for i, text in enumerate(labels):
    tk.Label(form_frame, text=text,
             bg="#f4f6f9").grid(row=i, column=0, pady=5)
    entry = tk.Entry(form_frame)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

entry_id, entry_name, entry_age, entry_email = entries

# Buttons
btn_frame = tk.Frame(root, bg="#f4f6f9")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12,
          command=add_student).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", width=12,
          command=update_student).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=12,
          command=delete_student).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Clear", width=12,
          command=clear_fields).grid(row=0, column=3, padx=5)

# Table
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(tree_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(tree_frame,
                    columns=("ID", "Name", "Age", "Email"),
                    show="headings",
                    yscrollcommand=scrollbar.set)

for col in ("ID", "Name", "Age", "Email"):
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

tree.bind("<ButtonRelease-1>", select_row)

# Pagination
pagination_frame = tk.Frame(root, bg="#f4f6f9")
pagination_frame.pack(pady=10)

tk.Button(pagination_frame, text="Previous",
          command=previous_page).pack(side=tk.LEFT, padx=5)

page_label = tk.Label(pagination_frame,
                      text="Page 1",
                      bg="#f4f6f9")
page_label.pack(side=tk.LEFT)

tk.Button(pagination_frame, text="Next",
          command=next_page).pack(side=tk.LEFT, padx=5)

view_students()

root.mainloop()