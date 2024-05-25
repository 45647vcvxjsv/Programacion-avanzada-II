import sqlite3

conexion = sqlite3.connect('Biblioteca.db')
cursor = conexion.cursor()

cursor.execute("DELETE FROM libros WHERE ano_de_publicacion < 2000")

conexion.commit()

conexion.close()

