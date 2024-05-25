import matplotlib.pyplot as plt 
import numpy as np 

x = range(200)
y = range(200) + np.random.randint(0, 20, 200)

plt.scatter(x,y)

plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('grafico de dispersion')
plt.grid(True)
plt.show()

 