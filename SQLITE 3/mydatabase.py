import mysql.connector

em = mysql.connector.connect(
    host="localhost",
    user="Abhishek", 
    password="@Abhishek2003",  
    database="mydatabase"  
)

cursor = em.cursor()
# cursor.execute('CREATE DATABASE new1')
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100),
            number INT,       
            position VARCHAR(100),
            salary INT
        )
    ''')
except:
    pass    

while True:
    print('\n1.add\n2.update\n3.delete\n4.search\n5.view all\n6.group by\n7.order by\n8.like\n9.join\n10.exit')
    ch = int(input('enter your choice: '))

    if ch == 1:
        l= int (input("Enter no> of employee : "))
        for i in range(l):
            id = int(input('enter employee id: '))
            name = input('enter your name: ')
            age = int(input('enter your age: '))
            email = input('enter your email: ')
            num=int(input('Enter phone  number:'))
            pos = input('enter position: ')
            salary = int(input('enter ur salary:'))

            cursor.execute('INSERT INTO employees (emp_id, name, age, email,number, position, salary) VALUES (%s, %s, %s, %s,%s, %s, %s)',
                        (id, name, age, email,num, pos, salary))
            em.commit()

    elif ch == 2:
        id = int(input('Enter ID of employee: '))
        name = input('Enter new name: ')
        age = int(input('Enter new age: '))
        email = input('Enter new email: ')
        num = input('Enter new phone number: ') 
        pos = input('Enter new position: ')
        sal = int(input('Enter your new salary: '))  
        cursor.execute('UPDATE employees SET name=%s, age=%s, email=%s, number=%s, position=%s, salary=%s WHERE emp_id=%s',
                    (name, age, email, num, pos, sal, id))

        em.commit()

    elif ch == 3:
        id = int(input('enter id of employee to delete: '))
        cursor.execute('DELETE FROM employees WHERE emp_id=%s', (id,))
        em.commit()

    elif ch == 4:
        id = int(input('enter id to search: '))
        cursor.execute('SELECT * FROM employees WHERE emp_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}{:<10}'.format('id', 'name', 'age', 'email','number' ,'position','salary'))
        print('-' * 85)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}{:<10}".format(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))
        else:
            print('id not available')

    elif ch == 5:
        cursor.execute('SELECT * FROM employees')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}{:<10}'.format('id', 'name', 'age', 'email','number' ,'position','salary'))
        print('-' * 85)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}{:<10}".format(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))

    elif ch ==6:
        cursor.execute("SELECT * FROM employees GROUP BY name")  
        data=cursor.fetchall()          
        for i in data:
            print(i)

    elif ch == 7:
        cursor.execute("SELECT * FROM employees ORDER BY salary ")    
        data=cursor.fetchall()    
        for i in data:
            print(i)

    elif ch== 8:
        a=input("enter the first letter of name you want to search:")    
        cursor.execute("SELECT * FROM employees WHERE name LIKE %s",(a,))    
        data=cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}{:<10}'.format('id', 'name', 'age', 'email','number' ,'position','salary'))
        print('-' * 85)
        for i in data:
                print("{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}{:<10}".format(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))

        
    elif ch == 9:
        cursor.execute("SELECT employees.emp_id,employees.name,employees.age,employees.email,employees.number,employees.position,employees.salary,dtls.address FROM employees INNER JOIN dtls on employees.emp_id=dtls.emp_id")
        data=cursor.fetchall()
        print('{:<10}{:<10}{:<15}{:<18}{:<20}{:<15}{:<10}{:<15}'.format('id', 'name', 'age', 'email','number' ,'position','salary','address'))
        print('-' * 100)
        for i in data:
                print("{:<10}{:<10}{:<10}{:<22}{:<22}{:<15}{:<10}{:<15}".format(i[0], i[1], i[2], i[3], i[4],i[5],i[6],i[7]))

    elif ch==10:
        break
    else:
        print('invalid choice.')