from abc import ABC, abstractclassmethod

class producto(ABC):
  def __init__(self, Nombre, Precio, Descripcion, Medico):
    self.Nombre = Nombre
    self.Precio = Precio
    self.Descripcion = Descripcion
    self.Medico = Medico

  def __str__(self):
    return f"Nombre: {self.Nombre}, Precio: {self.Precio}, Descripcion: {self.Descripcion}, Medico: {self.Medico}"

  @abstractclassmethod
  def metodo_abstracto(self):
    pass

class Lente(producto):
  def metodo_abstracto(self):
    pass

"""
Oftalmogia leopardo
Cotizacion de lentes de sol 
"""
Nombre = input("Ingrese el nombre del producto ")
Precio = float(input("Ingrese el valor de los lentes "))
Descripcion = input("Ingrese una breve descripcion del producto ")
Medico = input("Ingrese el Nombre del medico tratante ")


lente = Lente(Nombre, Precio, Descripcion, Medico)
print(lente)



