import sqlite3

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM appointments;")

data = cursor.fetchall()

print(data)

conn.close()