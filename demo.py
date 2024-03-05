import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="harsha",password="1234",database="harsha")

mycursor=mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

for i in result:
    print(i)