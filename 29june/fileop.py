import sqlite3

conn=sqlite3.connect("student.db")

cursor=conn.cursor()
# table creation
cursor.execute('''
               create table if not exists stud 
               (id interger primary key,
                name text not null,
               age integer null)
''')

print("created")

inserting data
id=int(input("enter your id :"))
name=input("enter your name:")
age=int(input("enter your age:"))
cursor.execute("insert into stud (id,name,age) values(?,?,?)",(id,name,age))
conn.commit()
print("data inserted")

# fetch entire row
cursor.execute("select * from stud")
r=cursor.fetchall()
print(r)
for i in r:
    print(i[0])

# single
id=int(input("enter your id:"))
cursor.execute("select * from stud where id=?",(id,))
r=cursor.fetchone()
print(r)

update
id=int(input("Enter id:"))
cursor.execute("select * from stud  where id=?",(id,))
r=cursor.fetchone()
print(r)
if id==r[0]:
    nname=input("enter new name:")
    cursor.execute("update stud set name=? where id=?",(nname,id))
    conn.commit()
    print("data updated")

else:
    print("no record found")

display
cursor.execute("select name from stud where age between ? and ?",(18 ,25))
e=cursor.fetchone()
print(e)
