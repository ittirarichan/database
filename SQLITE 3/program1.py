# # employee management system

# import sqlite3

# con=sqlite3.connect("database/sqlte3/prog1.db")
# try:
#     con.execute("create table staff(id int,name text ,age int ,email text,salary int)")
# except:
#     pass   

# while True:
#     print("1.add \n 2.update \n 3.delete \n 4.display \n 5.search \n 6.exit ")
#     ch=int(input("Enter your choice:"))
#     if ch == 1:
#         a=int(input("Enter no. of employees: "))
#         for i in range(a):
#             id=int(input("Enter id:"))
#             name=str(input("Enter name:"))
#             age=int(input("Enter age:"))
#             email=input("Enter email:")
#             salary=int(input("Enter salary:"))

#             con.execute("insert into staff(id,name,age,email,salary) values(?,?,?,?,?)",(id,name,age,email,salary))
#             con.commit()

#     elif ch == 2:
#         a = input("Enter name to update:")
#         b = input("Enter new name:")
#         con.execute("UPDATE staff SET name=? WHERE name=?", (b, a))
#         con.commit()


#     elif ch == 3:
#         a=input("Enter id to delete:")
#         con.execute("DELETE from staff WHERE id=?",(a,))
#         con.commit()

#     elif ch == 4:
#         data=con.execute("select * from staff")  
#         print("{:<6}{:<10}{:<6}{:<15}{:<10}".format("id","name", "age", "email","salary"))
#         print('_' * 50)
#         for i in data:
#             print("{:<6}{:<10}{:<6}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4]))

#     elif ch == 5:
#         a=input("Enter the id you want to search:") 
#         f=0       
#         data=con.execute("select * from staff where id=?",(a,))
#         print("{:<6}{:<10}{:<6}{:<15}{:<10}".format("id","name", "age", "email","salary"))
#         print('_' * 50)
#         for i in data:
#                 f=1
#                 print("{:<6}{:<10}{:<6}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4]))
#         if f==0:
#             print("sorry this name is not in the table")
#     elif ch == 6:
#         break

#     else:
#         print("invalid choice")