# Creating Database

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    dbs = cur.execute("create database klu_cse")
except:
    conn.rollback()

cur.close()
conn.close()

print("Hello World!")