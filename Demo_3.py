import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000")

cur = conn.cursor()

cur.execute("use pfsd")

print("Connected to PFSD Database")