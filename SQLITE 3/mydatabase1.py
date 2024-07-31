import mysql.connector

em=mysql.connector.connect(
    host="localhost",
    user="Abhishek", 
    password="@Abhishek2003",  
    database="mydatabase"  
)

cursor=em.cursor()
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dtls (
            emp_id INT PRIMARY KEY,
            address VARCHAR(100),
            position_name VARCHAR(100)  
        )
    ''')
except:
    pass
l= int (input("Enter no of employee : "))
for i in range(l):
            id = int(input('enter employee id: '))
            address=input("Enter address: ")
            pos=input("Enter the position: ")

            cursor.execute('INSERT INTO dtls (emp_id, address, position_name) VALUES (%s, %s, %s)',
                        (id,address,pos))
            em.commit()
# cursor.execute("DROP TABLE dtls")