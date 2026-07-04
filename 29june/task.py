import sqlite3
from reportlab.pdfgen import canvas

conn=sqlite3.connect("stud.db")

cursor=conn.cursor()
# table creation
cursor.execute('''
               create table if not exists student 
               (roll_no interger primary key,
                name text not null,
               sub1 integer not null,
               sub2 integer not null,
               sub3 integer not null
               )
''')

print("created")

print("What do you want to do?\n1.Add \n2.Update \n3.Read/View \n4.Search \n5.Delete \n6.View Result \n7.Exit")
ch=int(input(" Enter your choice:"))
match ch:
    case 1:
        roll_no=int(input("enter your roll_n :"))
        name=input("enter your name:")
        sub1=int(input("enter marks of sub1:"))
        sub2=int(input("enter marks of sub2:"))
        sub3=int(input("enter marks of sub3:"))
        cursor.execute("insert into student (roll_no,name,sub1,sub2,sub3) values(?,?,?,?,?)",(roll_no,name,sub1,sub2,sub3))
        conn.commit()
        print("data inserted")

    case 2:
        print("what do you want to do?" 
        "\n1.set marks 0 \n2.set multiple values of particular data\n3.set particular data")
        a=int(input("Enter your choice:"))
        match a:
            case 1:
                n=input("Enter sub to set value 0(sub1,sub2,sub3):")
                if n in ["sub1",'sub2','sub3']:
                    cursor.execute(f"update student set {n}=? ",(0,))
                    cursor.execute("select * from student")
                    r=cursor.fetchall()
                    print("Roll_no\tName\tSub1\tSub2\tSub3")
                    for i in r:
                        
                        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])


                    conn.commit()
                    
            case 2:
                roll_no=int(input("Enter roll_no to update the data:"))
                cursor.execute("select * from student  where roll_no=?",(roll_no,))
                r=cursor.fetchone()
                print(r)
                if roll_no==r[0]:
                    n=input("enter new name:")
                    s=int(input("enter marks of sub1:"))
                    s1=int(input("enter marks of sub2:"))
                    s2=int(input("enter marks of sub3:"))
                    cursor.execute("update student set name=?,sub1=?,sub2=?,sub3=? where roll_no=?",(n,s,s1,s2,roll_no))
                    cursor.execute("select * from student")
                    r=cursor.fetchall()
                    print("Roll_no\tName\tSub1\tSub2\tSub3")
                    for i in r:
                        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
                    conn.commit()
            
            case 3:
                pass
            case _:
                print("invalid choice")
    case 3:
        print("How to View the data ? \n1.View particular data \n2.View all data")
        a=int(input("enter your choice:"))
        match a:
            case 1:
                roll_no=int(input("Enter roll_no:"))
                cursor.execute("select * from student where roll_no=?",(roll_no,))
                r=cursor.fetchone()
                print("Roll_no\tName\tSub1\tSub2\tSub3")

                print(r[0],'\t',r[1],'\t',r[2],'\t',r[3],'\t',r[4])

            case 2:
                cursor.execute("select * from student")
                r=cursor.fetchall()
                print("Roll_no\tName\tSub1\tSub2\tSub3")
                for i in r:
                    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
    case 4:
        print("How do you want to search ? \n1.Search by rollno \n2.Search by name \n3.search by mark")
        a=int(input("enter your choice:"))
        match a:
            case 1:
                roll_no=int(input("enter a roll_no:"))
                cursor.execute("select * from student where roll_no=?",(roll_no,))
                r=cursor.fetchall()
                print("Roll_no\tName\tSub1\tSub2\tSub3")
                for i in r:
                    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])

            case 2:
                name=input("enter name :")
                cursor.execute("select * from student where name=? ",(name,))
                r=cursor.fetchall()
                print("Roll_no\tName\tSub1\tSub2\tSub3")
                for i in r:
                    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])

            case 3:
                m=int(input("enter marks:"))
                cursor.execute("select * from student where sub1=? or sub2=?or sub3=?",(m,m,m))
                r=cursor.fetchall()
                print("Roll_no\tName\tSub1\tSub2\tSub3")
                for i in r:
                    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
    
    case 5:
        print("How to Delete the data ? \n1.Delete particular data \n2.Delete all data")
        a=int(input("enter your choice:"))
        match a:
            case 1:
                roll_no=int(input("Enter roll_no:"))
                cursor.execute("delete from student where roll_no=?",(roll_no,))
                conn.commit()
                print("data deleted")

            case 2:
                cursor.execute("delete from student")
                conn.commit()
                print("data deleted")

    case 6:
        print("\n1.View Result\n2.Generate pdf")
        a=int(input("enter your choice:"))
        match a:
            case 1:
                roll_no=int(input("enter a roll_no:"))
                cursor.execute("select * from  student where roll_no=?",(roll_no,))
                r=cursor.fetchone()
                if r:
                    total=r[2]+r[3]+r[4]
                    p=total/3

                print("----Result-----")
                print("Name\tSub1\tSub2\tSub3\tTotal\tPercentage")
                print(r[1],'\t',r[2],'\t',r[3],'\t',r[4],'\t',total,'\t',p)
            case 2:
                roll_no=int(input("enter a roll_no:"))
                cursor.execute("select * from  student where roll_no=?",(roll_no,))
                r=cursor.fetchone()
                if r:
                    total=r[2]+r[3]+r[4]
                    p=total/3
                    c=canvas.Canvas(f"{r[1]}_result.pdf")
                    c.drawString(100,750,"----Result-----")
                    c.drawString(100,730,f"Roll_no: {r[0]}")
                    c.drawString(100,710,f"Name: {r[1]}")
                    c.drawString(100,690,f"Sub1: {r[2]}")
                    c.drawString(100,670,f"Sub2: {r[3]}")
                    c.drawString(100,650,f"Sub3: {r[4]}")
                    c.drawString(100,630,f"Total: {total}")
                    c.drawString(100,610,f"Percentage: {p}")
                    c.save()
                    print("pdf generated successfully")



    case 7:
        print("Thank You!!!!")

    case _:
        print("Invalid Choice")
