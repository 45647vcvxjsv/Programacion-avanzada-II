import matplotlib.pyplot as plt

# Parámetros de los profesores
profesores = {
  'Instructor': 945,
  'Asistente': 698,
  'Agregado': 736,
  'Asociado': 590
}

# Ordenar los profesores por puntaje en orden descendente
profesores_ordenados = sorted(profesores.items(), key=lambda x: x[1], reverse=True)

# Extraer los nombres y puntajes ordenados
nombres = [profesor[0] for profesor in profesores_ordenados]
puntajes = [profesor[1] for profesor in profesores_ordenados]

# Imprimir el ranking de profesores en pantalla
print("Ranking de profesores:")
for i, (nombre, puntaje) in enumerate(profesores_ordenados):
    print(f"{i+1}. {nombre}: {puntaje}")

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(nombres, puntajes, color='skyblue')
plt.xlabel('Profesores')
plt.ylabel('Puntaje')
plt.title('Ranking de Profesores por Puntaje')
plt.xticks(rotation=45)  
plt.tight_layout()

# Mostrar el gráfico
plt.show()

