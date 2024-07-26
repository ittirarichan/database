import sqlite3

con=sqlite3.connect("database/SQLITE 3/pgm1.db")
try:
    con.execute("create table dtls(name text ,place text ,nbr int ,address text)")
except:
    pass   

# a=int(input("Enter the number of the students: "))
# for i in range(a):
#     name=str(input("Enter name:"))
#     place=input("Enter place:")
#     nbr=int(input("Enter Phone number:"))
#     address=input("Enter address:")
#     con.execute("insert into dtls(name,place,nbr,address) values(?,?,?,?)",(name,place,nbr,address))
#     con.commit()


# data=con.execute("select staff.id,staff.name,staff.age,staff.email,staff.salary,dtls.place,dtls.nbr,dtls.address from staff inner join dtls on staff.name=dtls.name")
# print ("{:<10}{:<16}{:<10}{:<18}{:<16}{:<10}{:<20}{:<14}".format("id","name","age","email","salary","place","nbr","address"))
# for i in data:
#     print ("{:<10}{:<16}{:<10}{:<18}{:<16}{:<10}{:<20}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))


# data=con.execute("select staff.id,staff.name,staff.age,staff.email,staff.salary,dtls.place,dtls.nbr,dtls.address from staff left join dtls on staff.name=dtls.name")
# for i in data:
#     print (i)


data=con.execute("select staff.id,staff.name,staff.age,staff.email,staff.salary,dtls.place,dtls.nbr,dtls.address from staff right join dtls on staff.name=dtls.name")
for i in data:
    print (i)

