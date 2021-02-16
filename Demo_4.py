import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    dbs = cur.execute("show databases")
except:
    conn.rollback()

for i in cur:
    print(i)

cur.close()
conn.close()