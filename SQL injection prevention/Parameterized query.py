import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

username = input("Enter a username: ")
password = input("Enter a password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

results = cursor.fetchall()
