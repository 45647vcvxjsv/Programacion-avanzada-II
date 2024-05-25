import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('medicamentos.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    laboratorio TEXT,
    mg INTEGER,
    fecha_elaboracion TEXT,
    fecha_vencimiento TEXT,
    presentacion TEXT
)
''')

# Insertar datos
medicamentos = [
    ('Paracetamol', 'Lab Farma', 500, '2023-01-15', '2025-01-15', 'capsulas'),
    ('Ibuprofeno', 'MediCorp', 400, '2022-12-01', '2024-12-01', 'capsulas'),
    ('Amoxicilina', 'BioPharm', 250, '2023-03-10', '2025-03-10', 'capsulas'),
    ('Cefalexina', 'PharmaPlus', 500, '2023-05-20', '2025-05-20', 'capsulas'),
    ('Diclofenaco', 'SaludTech', 50, '2023-06-05', '2024-06-05', 'capsulas'),
    ('Loratadina', 'MedLab', 10, '2023-04-25', '2025-04-25', 'capsulas'),
    ('Omeprazol', 'GastroLab', 20, '2023-07-15', '2025-07-15', 'capsulas'),
    ('Azitromicina', 'AntibioTech', 500, '2023-02-28', '2025-02-28', 'capsulas'),
    ('Metformina', 'DiabeCare', 850, '2023-01-20', '2025-01-20', 'capsulas'),
    ('Levotiroxina', 'EndoPharma', 50, '2023-03-30', '2025-03-30', 'capsulas'),
    ('Clorfenamina', 'AllerLab', 4, '2023-05-10', '2024-05-10', 'capsulas'),
    ('Ranitidina', 'AcidControl', 150, '2023-02-15', '2025-02-15', 'capsulas'),
    ('Cetirizina', 'HistamineStop', 10, '2023-06-01', '2025-06-01', 'capsulas'),
    ('Prednisona', 'SteroidLab', 5, '2023-01-05', '2025-01-05', 'capsulas'),
    ('Clindamicina', 'BioPharm', 300, '2023-02-10', '2025-02-10', 'capsulas')
]

cursor.executemany('''
INSERT INTO medicamentos (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion)
VALUES (?, ?, ?, ?, ?, ?)
''', medicamentos)

# Guardar (commit) los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tabla 'medicamentos' creada con éxito.")
