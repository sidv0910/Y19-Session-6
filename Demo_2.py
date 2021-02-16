import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="0000")

if mydb:
    print("Connected to Database")
else:
    print("Unable to Connect to Database")