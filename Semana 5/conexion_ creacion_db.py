import sqlite3

conexion = sqlite3.connect('Biblioteca.db')

cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS libros
                (id INTEGER PRIMARY KEY,
                titulo_del_libro VARCHAR,
                codigo_del_libro INTEGER,
                ano_de_publicacion DATE,
                autor VARCHAR,
                editorial VARCHAR)''')


cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Anastacia', 10, 2012, 'Silvio Castardo', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Reino Olvidado', 11, 1965, 'Aylee', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Starcraft 2', 13, 2023, 'Solji', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Starcraft 1', 45, 1996, 'Anelisse Michell', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Oblivion', 17, 2012, 'Melissa Perez', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Anatomia del Cuerpo', 56, 2015, 'Carlos Fuentes', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Analisis del Mercado', 15, 2011, 'Jesus Garcia', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Helion', 03, 1987, 'Marcela Barrios', 'Planeta')")
cursor.execute("INSERT INTO libros (titulo_del_libro, codigo_del_libro, ano_de_publicacion, autor, editorial) VALUES ('Metastasis', 56, 2016, 'Esteban Cifuentes', 'Planeta')")

conexion.commit()
conexion.close()

