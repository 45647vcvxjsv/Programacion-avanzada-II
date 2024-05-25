import pandas as pd
import random
import datetime

nombres = ["Juan", "Maria", "Soledad", "Laura", "Ana", "Carlos", "Sofía", "Luis", "Elena", "Diego"]
apellidos = ["Gómez", "Pérez", "Martínez", "Rodríguez", "López", "González", "Hernández", "Díaz", "Sánchez", "Torres"]
especialidades = ["Cardiología", "Pediatría", "Oncología", "Neurología", "Ginecología", "Dermatología", "Psiquiatría", "Endocrinología", "Oftalmología", "Cirugía"]
sexos = ["Masculino", "Femenino"]
direcciones = ["Calle Principal 123", "Avenida Central 456", "Plaza Mayor 789", "Callejón Secreto 321", "Camino Real 654"]

data = []
for i in range(50):
  # Crea un diccionario para cada doctor
  doctor = {
      'Nombre': random.choice(nombres),
      'Apellido': random.choice(apellidos),
      'Especialidades': random.choice(especialidades),
      'Sexo': random.choice(sexos),
      'Direcciones': random.choice(direcciones)
  }
  # Agrega el diccionario que contiene los datos del doctor a la lista data
  data.append(doctor)

nombre_archivo = 'Lista_de_medicos_{}.csv'.format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

df = pd.DataFrame(data)

df.to_csv('Lista de medicos completa', index=False)

print("Archivo CSV generado completamente")

