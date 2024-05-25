class Libreria:
    def __init__(self, nombre, autor, Stock_de_libros, genero, editorial, fecha_edicion, pais_edicion):
        self.nombre = nombre
        self.autor = autor
        self.Stock_de_libros = Stock_de_libros
        self.genero = genero
        self.editorial = editorial
        self.pais_edicion = pais_edicion
        self.__fecha_edicion = fecha_edicion
  
    def __str__(self):
        return f"""
        Nombre: {self.nombre}
        Autor: {self.autor}
        Stock_de_libros: {self.Stock_de_libros}
        Genero: {self.genero}
        Editorial: {self.editorial}
        Fecha de edicion: {self.get_fecha_edicion()}  
        Pais de edicion: {self.pais_edicion}
        """

    def get_fecha_edicion(self):
        return self.__fecha_edicion

def Obtener_informacion_libreria():
    libros = []
    for i in range(5):
        nombre = input("Ingrese el Nombre del libro: ")
        autor = input("Ingrese el Autor del libro: ")
        Stock_de_libros = input("Ingrese el Stock de los libros: ")
        genero = input("Ingrese el Genero de los libros: ")
        editorial = input("Ingrese la Editorial de los libros: ")
        fecha_edicion = input("Ingrese la Fecha de edicion de los libros: ")
        pais_edicion = input("Ingrese la nacionalidad de los libros: ")
        libros.append(Libreria(nombre, autor, Stock_de_libros, genero, editorial, fecha_edicion, pais_edicion))
    return libros


libros = Obtener_informacion_libreria()

for libro in libros:
    print(libro)
