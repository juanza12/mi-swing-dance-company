import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE estudiantes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
edad INTEGER,
telefono TEXT,
clase TEXT,
fecha TEXT
)
""")

conn.commit()
conn.close()

print("Base de datos creada")