import sqlite3

# Conectar a la base de datos SQLite (se creará si no existe)
conn = sqlite3.connect('medicos.db')
cursor = conn.cursor()

# Crear tabla de médicos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Medico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    direccion TEXT,
    especialidad TEXT
)
''')

# Datos ficticios de médicos
medicos = [
    ("Ana", "Martinez", "Calle Falsa 123", "Cardiología"),
    ("Luis", "González", "Avenida Siempre Viva 742", "Dermatología"),
    ("Carlos", "López", "Calle Larga 456", "Gastroenterología"),
    ("Marta", "Pérez", "Calle Corta 789", "Neurología"),
    ("Juan", "Hernández", "Avenida Central 101", "Pediatría"),
    ("Lucía", "Díaz", "Calle Peatonal 202", "Oftalmología"),
    ("José", "Sánchez", "Calle Ancha 303", "Ortopedia"),
    ("María", "Ramírez", "Avenida Principal 404", "Psiquiatría"),
    ("Pedro", "Torres", "Callejón Sin Salida 505", "Ginecología"),
    ("Carmen", "Flores", "Paseo de la Reforma 606", "Urología"),
    ("Jorge", "Castro", "Callejón de los Milagros 707", "Oncología"),
    ("Elena", "Morales", "Avenida del Sol 808", "Endocrinología"),
    ("Roberto", "Ortega", "Calle del Río 909", "Hematología"),
    ("Sofía", "Vargas", "Plaza Mayor 111", "Neumología"),
    ("David", "Ruiz", "Bulevar de los Sueños 222", "Nefrología"),
    ("Laura", "Jiménez", "Avenida del Parque 333", "Reumatología"),
    ("Fernando", "Mendoza", "Calle del Mar 444", "Otorrinolaringología"),
    ("Patricia", "Cruz", "Avenida del Bosque 555", "Alergología"),
    ("Antonio", "Herrera", "Calle de la Paz 666", "Infectología"),
    ("Gabriela", "Rojas", "Calle del Amor 777", "Medicina Interna")
]

# Insertar datos ficticios en la tabla Medico
cursor.executemany('''
INSERT INTO Medico (nombre, apellido, direccion, especialidad)
VALUES (?, ?, ?, ?)
''', medicos)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

print("Datos de médicos ingresados correctamente en la base de datos.")
