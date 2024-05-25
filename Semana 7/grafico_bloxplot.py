import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generar datos para las series
datos_serie1 = np.random.normal(loc=750, scale=np.sqrt(50), size=700)
datos_serie2 = np.random.normal(loc=800, scale=np.sqrt(60), size=700)
datos_serie3 = np.random.normal(loc=700, scale=np.sqrt(40), size=700)

# Configurar el estilo de seaborn para una apariencia más atractiva
sns.set(style="whitegrid")

# Crear la figura y los ejes para personalización avanzada
fig, ax = plt.subplots(figsize=(12, 6))

# Trazar el boxplot utilizando seaborn (mejor manejo de estilos)
sns.boxplot(data=[datos_serie1, datos_serie2, datos_serie3], 
            orient='h',  # Horizontal
            palette="Set3",  # Paleta de colores
            saturation=0.75,  # Intensidad de los colores
            width=0.6,  # Ancho de las cajas
            ax=ax)  # Usar los ejes personalizados

# Personalización adicional del gráfico
ax.set_xlabel('Valor', fontsize=12)
ax.set_ylabel('Distribución', fontsize=12)
ax.set_title('Distribución Normal - Serie 1, Serie 2 y Serie 3', fontsize=14)

# Mostrar el gráfico
plt.show()






'''
datos_serie1 = np.random.normal(750, np.sqrt(50), 700)
datos_serie2 = np.random.normal(900, np.sqrt(20), 700)
datos_serie3 = np.random.normal(500, np.sqrt(40), 700)

plt.figure(figsize=(12, 6))  # Ajusta el tamaño del gráfico

# Boxplot para las tres series
plt.boxplot([datos_serie1, datos_serie2, datos_serie3], labels=['Serie 1', 'Serie 2', 'Serie 3'], 
           notch=True, vert=False, patch_artist=True)  # Personaliza el boxplot

# Personalización del gráfico
plt.xlabel('Distribución')
plt.ylabel('Valor')
plt.title('Distribución normal - Serie 1, Serie 2 y Serie 3')
plt.grid(True)
plt.show()

'''
