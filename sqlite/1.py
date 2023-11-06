import sqlite3
from b.rest import Restaurant

connection = sqlite3.connect("database.db")

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tables (
id INTEGER PRIMARY KEY,
seats TEXT NOT NULL
is_reserved INTEGER
)
''')
cursor.execute('INSERT INTO Tables (id, seats, is_reserved) VALUES (?, ?, ?)',
               (0, Restaurant.tables_num[0].seats, Restaurant.tables_num[0].is_reserved))

connection.commit()
connection.close()
