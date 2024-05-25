import pandas as pd
import random


nombres = ["Juan", "Maria", "Soledad", "Laura", "Ana", "Carlos", "Sofía", "Luis", "Elena", "Diego"]
apellidos = ["Gómez", "Pérez", "Martínez", "Rodríguez", "López", "González", "Hernández", "Díaz", "Sánchez", "Torres"]
especialidades = ["Cardiología", "Pediatría", "Oncología", "Neurología", "Ginecología", "Dermatología", "Psiquiatría", "Endocrinología", "Oftalmología", "Cirugía"]
sexos = ["Masculino", "Femenino"]
direcciones = ["Calle Principal 123", "Avenida Central 456", "Plaza Mayor 789", "Callejón Secreto 321", "Camino Real 654"]

data = []
for i in range(50):
  doctor = {
      'Nombre': random.choice(nombres),
      'Apellido': random.choice(apellidos),
      'Especialidades': random.choice(especialidades),
      'Sexo': random.choice(sexos),
      'Direcciones': random.choice(direcciones)
  }
  data.append(doctor)


df = pd.DataFrame(data)

doctores_hombres = df[df['Sexo'] == 'Masculino']
doctores_mujeres = df[df['Sexo'] == 'Femenino']

print("Doctores Hombres")
print(doctores_hombres)

print("Doctores mujeres")
print(doctores_mujeres)


