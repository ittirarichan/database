# import sqlite3

# con=sqlite3.connect("sample.db")  #connection

# try:
#     con.execute("Create table student(age int,name text,mark real)")  #creatw table
# except:
#     pass
# con.execute("insert into student(age,name,mark) values(22,'Akshay',65)")   #add a value
# con.commit() #to save




# import sqlite3

# con=sqlite3.connect("sample1.db")  #connection

# try:
#     con.execute("Create table student(age int,name text,mark real)")  #creatw table
# except:
#     pass
# a=int(input("Enter the number of students"))
# for i in range (a):
#     age=int(input("Age"))
#     name=input("Name")
#     mark=float(input("Mark"))

#     con.execute("insert into student(age,name,mark) values(?,?,?)",(age,name,mark))   #add a value
#     con.commit() #to save




# import sqlite3

# con=sqlite3.connect("sample1.db")  #connection

# try:
#     con.execute("Create table student(age int,name text,mark real)")  #creatw table
# except:
#     pass
# data=con.execute("select * from student")
# for i in data:
#     print(i)



# import sqlite3

# con=sqlite3.connect("sample1.db")  #connection

# try:
#     con.execute("Create table student(age int,name text,mark real)")  #creatw table
# except:
#     pass
# a=int(input("Enter the number of students"))
# for i in range (a):
#     age=int(input("Age"))
#     name=input("Name")
#     mark=float(input("Mark"))

#     con.execute("insert into student(age,name,mark) values(?,?,?)",(age,name,mark))   #add a value
#     con.commit() #to save
# data=con.execute("select * from student")
# print("{:<10}{:<10}{:<10}".format('age','name','mark'))
# print("=" * 24)

# for i in data:
#     print("{:<10}{:<10}{:<10}".format(i[0],i[1],i[2]))





# import sqlite3
# con=sqlite3.connect("database/SQLITE 3/sample1.db")
# name=str(input("name"))
# data=con.execute("select * from student where name=?",(name,))
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# import sqlite3
# con=sqlite3.connect("database/SQLITE 3/sample1.db")
# data=con.execute("select * from student where mark>=60")
# print("{:<10}{:<16}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))



# import sqlite3
# con=sqlite3.connect("database/SQLITE 3/sample1.db")
# data=con.execute("update student set name='ABHISHEK BINISH' where name='abhi'")
# con.commit()
# data=con.execute("select * from student where name='ABHISHEK BINISH'")
# print("{:<15}{:<15}{:<10}".format("age","name","mark"))
# for i in data:
#     print("{:<10}{:<20}{:<10}".format(i[0],i[1],i[2]))




# import sqlite3
# con=sqlite3.connect("database/SQLITE 3/sample1.db")
# data=con.execute("Select * from student where name like '_a%' ")
# print ("{:10}{:16}{:10}".format("age","name","mark"))
# for i in data:
#     print ("{:10}{:16}{:10}".format(i[0],i[1],i[2]))





# import sqlite3
# con=sqlite3.connect("database/SQLITE 3/sample1.db")
# data=con.execute("Select * from student order by name desc")
# print ("{:10}{:10}{:6}".format("age","name","mark"))
# for i in data:
#     print ("{:10}{:10}{:6}".format(i[0],i[1],i[2]))





# import sqlite3
# con=sqlite3.connect("database/SQLITE 3/sample1.db")
# data=con.execute("Select name, count(mark) from student group by name")
# print ("{:10}{:10}{:6}".format("age","name","mark"))
# for i in data:
#     print(i)





import sqlite3
con=sqlite3.connect("database/SQLITE 3/sample1.db") 

try:
    con.execute("Create table employee (name text,age int,salary real)") 
except:
    pass
a=int(input("Enter the number of employees"))
for i in range (a):
    name=input("Name")
    age=int(input("Age"))
    mark=float(input("salary"))

    con.execute("insert into employee(name,age,salary) values(?,?,?)",(name,age,)) 
    con.commit()
data=con.execute("select * from employee")
print("{:<10}{:<10}{:<10}".format('age','name','salary'))
print("=" * 24)

for i in data:
    print("{:<10}{:<10}{:<10}".format(i[0],i[1],i[2]))

