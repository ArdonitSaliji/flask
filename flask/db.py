import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ardonit"
)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)