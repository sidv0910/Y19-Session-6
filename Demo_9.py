# Fetching Rows from Database
# fetchall()
# fetchone()

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000", database="klu_cse")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    cur.execute("select * from student order by branch desc")
    result = cur.fetchone()
    for i in result:
        print(i)
    conn.commit()
    print("Record Inserted Successfully")
except:
    conn.rollback()
print(cur.rowcount, "Records Inserted")

cur.close()
conn.close()