# Solicitar información sobre el primer animal en peligro de extinción
nombre_animal_1 = input("Ingrese el nombre del primer animal en peligro de extinción: ")
especie_animal_1 = input("Ingrese la especie del primer animal en peligro de extinción: ")
distribucion_animal_1 = input("Ingrese la distribución del primer animal en peligro de extinción: ")
estado_animal_1 = input("Ingrese el estado de conservación del primer animal en peligro de extinción: ")
peso_animal_1 = float(input("Ingrese el peso del primer animal en peligro de extinción (en kg): "))

# Solicitar información sobre el segundo animal en peligro de extinción
nombre_animal_2 = input("Ingrese el nombre del segundo animal en peligro de extinción: ")
especie_animal_2 = input("Ingrese la especie del segundo animal en peligro de extinción: ")
distribucion_animal_2 = input("Ingrese la distribución del segundo animal en peligro de extinción: ")
estado_animal_2 = input("Ingrese el estado de conservación del segundo animal en peligro de extinción: ")
peso_animal_2 = float(input("Ingrese el peso del segundo animal en peligro de extinción (en kg): "))

# Solicitar información sobre el tercer animal en peligro de extinción
nombre_animal_3 = input("Ingrese el nombre del tercer animal en peligro de extinción: ")
especie_animal_3 = input("Ingrese la especie del tercer animal en peligro de extinción: ")
distribucion_animal_3 = input("Ingrese la distribución del tercer animal en peligro de extinción: ")
estado_animal_3 = input("Ingrese el estado de conservación del tercer animal en peligro de extinción: ")
peso_animal_3 = float(input("Ingrese el peso del tercer animal en peligro de extinción (en kg): "))

# Calcular el promedio de peso
promedio_peso = (peso_animal_1 + peso_animal_2 + peso_animal_3) / 3

# Imprimir información sobre los animales en extinción
print("Información sobre animales en peligro de extinción:")
print("1. Nombre:", nombre_animal_1)
print("   Especie:", especie_animal_1)
print("   Distribución:", distribucion_animal_1)
print("   Estado de conservación:", estado_animal_1)
print("   Peso:", peso_animal_1, "kg")
print()
print("2. Nombre:", nombre_animal_2)
print("   Especie:", especie_animal_2)
print("   Distribución:", distribucion_animal_2)
print("   Estado de conservación:", estado_animal_2)
print("   Peso:", peso_animal_2, "kg")
print()
print("3. Nombre:", nombre_animal_3)
print("   Especie:", especie_animal_3)
print("   Distribución:", distribucion_animal_3)
print("   Estado de conservación:", estado_animal_3)
print("   Peso:", peso_animal_3, "kg")
print()
print("El promedio de peso de los animales en extinción es:", promedio_peso, "kg")