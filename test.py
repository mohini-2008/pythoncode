import mysql.connector

print("Program Started")
conn = mysql.connector.connect(
    host="localhost",
    # port=3306,
    user="root",
    password="Mohini@08",
    database="demo",
    use_pure=True
)

print("Database Connected Successfully")

cursor=conn.cursor()
cursor.execute("""
        create table if not exists emp(
            empid int primary key auto_increment,
            name varchar(20) not null,
            sal decimal(10,2) check(sal>0)
            )
""")
conn.commit()
print("table created")

