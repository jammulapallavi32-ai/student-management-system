import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="password",
    database="student_db"
)

cursor = conn.cursor()

print("Database Connected Successfully!")