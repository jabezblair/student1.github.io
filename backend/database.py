import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="resume_ai"
)

cursor = db.cursor()
