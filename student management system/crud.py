from db import get_connection
from student import student
from user import user

def add_stud():
    conn=get_connection()
    cursor=conn.cursor()
    name=input("enter your name:")
    age=int(input("enter your age:"))
    email=input("enter your mail id:")
    obj=student(name,age,email)
    query="insert into student (name,age,email) values(%s,%s,%s)"
    values=(obj.name,obj.age,obj.email)
    cursor.execute(query,values)
    conn.commit()
    print("student added!")

#add_stud()

def add_user():
    conn=get_connection()
    cursor=conn.cursor()
    username=input("enter your username:")
    password=input("enter your password:")
    role=input("enter your role:")
    obj=user(username,password,role)
    query="insert into login(username,password,role) values(%s,%s,%s)"
    values=(obj.username,obj.password,obj.role)
    cursor.execute(query,values)
    conn.commit()
    print("user added!")

# add_user()

def view_stud():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    return rows

# print(view_stud())


