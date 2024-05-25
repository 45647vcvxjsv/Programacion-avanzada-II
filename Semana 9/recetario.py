import sqlite3

conn = sqlite3.connect('medicos.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM medico')

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
