from crud import *
from db import get_connection

def login():
    conn=get_connection()
    cursor=conn.cursor()
    username=input("enter your username:")
    password=input("enter your password:")
    cursor.execute("select role from login where username=%s",(username,))
    row=cursor.fetchone()

    if row[0]=='admin':
        print("1.add user to main app\t2.add student\t3.view student\t4.exit\t")
        ch=int(input("\nenter your choice:"))
        match(ch):
            case 1:
                add_user()
            case 2:
                add_stud()
            case 3:
                print(view_stud())
            case 4:
                print("exit")
            case _:
                print("invalid choice:")
       

    elif row[0]=='user':
        print("1.view students:")
        ch=int(input("\nenter your choice:"))
        match(ch):
            case 1:
                print(view_stud())


        

login()
