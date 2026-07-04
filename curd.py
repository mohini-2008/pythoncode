from test import conn,cursor

def insert_value():
    name=input("enter name:")
    sal=int(input("enter salary:"))

    query = "INSERT INTO emp(name, sal) VALUES (%s, %s)"
    values = (name, sal)

    cursor.execute(query, values)
    conn.commit()

    print("Employee added successfully!")
