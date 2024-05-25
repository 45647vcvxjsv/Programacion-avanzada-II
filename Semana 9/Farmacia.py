class Persona:
    def __init__(self, Nombre, Apellido, Direccion):
        self.nombre = Nombre
        self.apellido = Apellido
        self.direccion = Direccion

    def actualizarDatos(self, Nombre, Apellido, Direccion):
        self.nombre = Nombre
        self.apellido = Apellido
        self.direccion = Direccion

    def datosPersona(self):
        return f"Cliente: {self.nombre}, Apellido: {self.apellido}, Direccion: {self.direccion}"


class Paciente(Persona):
    def __init__(self, Nombre, Apellido, Rut, Edad, Direccion):
        super().__init__(Nombre, Apellido, Direccion)
        self.rut = Rut
        self.edad = Edad

    def actualizarDatos(self, Nombre, Apellido, Edad, Direccion):
        super().actualizarDatos(Nombre, Apellido, Direccion)
        self.edad = Edad

    def mostrarDatos(self):
        return f"Paciente: Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Direccion: {self.direccion}, RUT: {self.rut}"


class Medico:
    def __init__(self, Nombre, Apellido, Direccion, Especialidad):
        self.nombre = Nombre
        self.apellido = Apellido
        self.direccion = Direccion
        self.especialidad = Especialidad

    def mostrarInfoMedico(self):
        return f"Medico: Profesional: {self.nombre}, Apellido: {self.apellido}, Especialidad: {self.especialidad}"


class RecetaMedica:
    def __init__(self, NombreMedico, Diagnostico, FechaEmision):
        self.nombreMedico = NombreMedico
        self.diagnostico = Diagnostico
        self.fechaEmision = FechaEmision

    def mostrarReceta(self):
        return f"Receta: Nombre Profesional: {self.nombreMedico}, Diagnostico: {self.diagnostico}, FechaEmision: {self.fechaEmision}"


class Medicamento:
    def __init__(self, nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.mg = mg
        self.fecha_elaboracion = fecha_elaboracion
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_medicamento(self):
        return f"Medicamento Recetado: {self.nombre}, Laboratorio: {self.laboratorio}, Miligramos: {self.mg}, Fecha de elaboracion: {self.fecha_elaboracion}, Fecha Vencimiento: {self.fecha_vencimiento}"


# Crear objetos y mostrar información
infoPaciente1 = Paciente("Jose", "Cifuentes", "12336547-7", 35, "Marques 55")
print(infoPaciente1.mostrarDatos())

medico1 = Medico("Marcela", "Santelices", "Casrell 23", "Traumatologo")
print(medico1.mostrarInfoMedico())

receta1 = RecetaMedica("Marcela Santelices", "Hipertension", "2024-12-15")
print(receta1.mostrarReceta())

Dosis_medicamento = Medicamento(
    "Paracetamol", "Lab Farma", 500, "2023-01-15", "2025-01-15")
print(Dosis_medicamento.mostrar_medicamento())
