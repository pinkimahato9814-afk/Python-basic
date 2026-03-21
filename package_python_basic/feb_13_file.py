# ile = open("samplefile.txt", "w")f
# file.write("This is a file created on February 13th.\n "*30)
# file.close()


# with open("samplefile.txt", "a") as file:
#  file.write("This is a file created on February 13th.\n "*30)


# how we read file
# with open("samplefile.txt", "r") as file:
#     content = file.read()
#     for i in content:
#        print(i)


# file = open("samplefile1.txt", "r")
# data = file.read()
# print(data)
# file.close()


#write a program for user demogrphyics important points take  name age  and address from terminal and write in file

# file =open("user_data.txt", "w")
# for i in range(3):
#      name = input("Enter your name: ")
#      age = input("Enter your age: ")
#      address = input("Enter your address: ")

#      file.writelines(f"Name: {name}\nAge: {age}\nAddress: {address}\n")
#      file.writelines(f"*"*50+"\n")
# file.close()

# same work how can do by using recursion function
# def user_data_entry(n):
#     if n>0:
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         address = input("Enter your address: ")

#         with open("user_data.txt", "a") as file:
#             file.writelines(f"Name: {name}\nAge: {age}\nAddress: {address}\n")
#             file.writelines(f"*"*50+"\n")

#     user_data_entry(n-1)


# # how can import csv file  in python
# import csv
# with open("sample.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)


 #incomplet code
# import csv
# data_to_write =[['name','department','birthdaymonth'],['pinki','HR','February'], ['rita','Finance','March']]
                
# with open("sample1.csv", "w", newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data_to_write)


# import csv

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})



# with open('names.csv', newline='') as ftpr:
#     reader = csv.DictReader(ftpr)
#     my_obj = {'name':"pinki", 'age':25, 'city':"bangalore"}


#i want to study json format file
# import json
# json_data = [
#     {"name": "pinki"},
#     {"address": "kalipur"},
#     {"age": 23},
#     12, 56, 45, 56,
#     [465,87,89]
# ]

# #open file in write mood
# with open('data3.json','w') as file:
#     json.dump(json_data, file ,indent =4)

# print("json data is successfully created .......!!!!!!!")    


    

# # file handling by using file try and except  method 
# import json
# import os
# json_data = [
#     {"name": "pinki"},
#     {"address": "kalipur"},
#     {"age": 23},
#     12, 56, 45, 56,
#     [465,87,89]
# ]

# file_name  = 'data3.json'
# try:
#     # check data is valid or not
#     if isinstance(json_data,(list,dict)):
#         with open('data3.json','w') as file:
#          json.dump(json_data, file ,indent =4)

#     print("json data is successfully created .......!!!!!!!")    

# except Exception as e:
#     print("Error:", e)

# Mode	Meaning
# "r"	Read (default)
# "w"	Write (overwrites file)
# "a"	Append (adds to file)
# "x"	Create new file
# "rb"	Read binary
# "wb"	Write binary

    
file = open("pinki.txt", "w")
file.write("This is a file created on February 13th.\n "*30)