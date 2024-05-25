class Animal:
    def __init__(self, nombre, especie, distribucion, estado, peso):
        self.nombre = nombre
        self.especie = especie
        self.distribucion = distribucion
        self.estado = estado
        self.peso = peso
  
    def __str__(self):
      return f"Informacion sobre el animal:\nNombre: {self.nombre}\nEspecie: {self.especie}\nDistribucion: {self.distribucion}\nEstado: {self.estado}\nPeso: {self.peso} kg"


    def calcular_peso_animal(self):
        self.peso += self.peso * 0.1

def obtener_info_de_animales():
    animales = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre del animal {i + 1} en extincion: ")
        especie = input(f"Ingrese la especie del animal {i + 1} en extincion: ")
        distribucion = input(f"Ingrese la distribucion del animal {i + 1}: ")
        estado = input(f"Ingrese el estado del animal {i + 1}: ")
        peso = float(input(f"Ingrese el peso del animal {i + 1} (en KG): "))
        
        animal = Animal(nombre, especie, distribucion, estado, peso)
        animales.append(animal)

    for animal in animales:
        animal.calcular_peso_animal()

    promedio_peso = sum(animal.peso for animal in animales) / len(animales)

    print("Informacion sobre los animales en extincion: ")
    for animal in animales:
        print(animal)

    print(f"El promedio del peso del animal en los 6 primeros meses en el area protegida es de {promedio_peso:.2f} KG")

if __name__ == "__main__":
    obtener_info_de_animales()

  