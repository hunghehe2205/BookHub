import mysql.connector

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="0329782205",
    database="ebook"
)

# Create a cursor object
cursor = mydb.cursor()
