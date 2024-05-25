from abc import ABC, abstractclassmethod

class producto(ABC):
  def __init__(self, Nombre, Precio,Descripcion, Medico):
    self.Nombre = Nombre
    self.Precio = Precio
    self.Descripcion = Descripcion
    self.Medico = Medico
  
  def __str__(self):
    return f"Nombre: {self.Nombre}, Precio: {self.Precio}, Descripcion: {self.Descripcion}, Medico: {self.Medico}"
  

  
  def get_Nombre(self):
    return self.Nombre
  def set_Nombre(self,Nombre):
    self.Nombre = Nombre
  def get_Precio(self):
    return self.Precio
  def set_Precio(self, Precio):
    self.Precio = Precio
  def get_Descripcion(self):
    return self.Descripcion
  def set_Descripcion(self, Descripcion):
    self.Descripcion = Descripcion
  def get_Medico(self):
    return self.Medico
  def set_Medico(self, Medico):
    self.Medico = Medico

  @abstractclassmethod
  def metodo_abstracto(self):
    pass

class Lente(producto):
  def metodo_abstracto(self):
    pass  


lente = Lente("Marco Vision", 100, "De Sol", "Juan")
print(lente)

