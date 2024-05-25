import numpy as np 
import matplotlib.pyplot as plt 

media = 500
variacion = 40 
num_registros = 700 

datos = np.random.normal(loc=media, scale=np.sqrt(variacion), size=num_registros)

plt.figure(figsize=(10,6))
plt.hist(datos, bins=30, density=True, alpha=0.75, color='skyblue', edgecolor='black')
desviacion_estandar = np.sqrt(variacion)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Media = {media}')
plt.axvline(media - desviacion_estandar, color='green', linestyle='dashed', linewidth=1.5, label='±1 Desviación Estándar')
plt.axvline(media + desviacion_estandar, color='green', linestyle='dashed', linewidth=1.5)

plt.xlabel('valores')
plt.ylabel('densidad')
plt.title('distribucion normal')
plt.legend()

plt.show()

