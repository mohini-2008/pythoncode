import mysql.connector as x
 
def get_connection():
    conn=x.connect(
        host="localhost",
        user="root",
        password="Mohini@08",
        database="sms_linkcode",
        use_pure=True
    )
    print("database connected")
    return conn

print(get_connection())