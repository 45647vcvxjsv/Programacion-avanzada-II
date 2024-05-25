import tkinter as tk
from tkinter import ttk
import sqlite3

# Definición de las clases


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

# Configuración de la base de datos


def setup_database():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pacientes (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT,
                        apellido TEXT,
                        rut TEXT,
                        edad INTEGER,
                        direccion TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Medicos (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT,
                        apellido TEXT,
                        direccion TEXT,
                        especialidad TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Recetas (
                        id INTEGER PRIMARY KEY,
                        nombre_medico TEXT,
                        diagnostico TEXT,
                        fecha_emision TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Medicamentos (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT,
                        laboratorio TEXT,
                        mg INTEGER,
                        fecha_elaboracion TEXT,
                        fecha_vencimiento TEXT)''')
    conn.commit()
    conn.close()

# Clase principal del formulario Tkinter


class Formulario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario")
        self.geometry("400x400")

        # Variables de entrada
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.direccion_var = tk.StringVar()
        self.rut_var = tk.StringVar()
        self.edad_var = tk.IntVar()
        self.especialidad_var = tk.StringVar()
        self.diagnostico_var = tk.StringVar()
        self.fecha_emision_var = tk.StringVar()
        self.medicamento_var = tk.StringVar()
        self.laboratorio_var = tk.StringVar()
        self.mg_var = tk.IntVar()
        self.fecha_elab_var = tk.StringVar()
        self.fecha_venc_var = tk.StringVar()

        # Widgets del formulario
        self.create_widgets()

    def create_widgets(self):
        # Labels y Entradas
        ttk.Label(self, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.nombre_var).grid(row=0, column=1)

        ttk.Label(self, text="Apellido:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.apellido_var).grid(row=1, column=1)

        ttk.Label(self, text="Direccion:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.direccion_var).grid(row=2, column=1)

        ttk.Label(self, text="RUT:").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.rut_var).grid(row=3, column=1)

        ttk.Label(self, text="Edad:").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.edad_var).grid(row=4, column=1)

        ttk.Label(self, text="Especialidad:").grid(
            row=5, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.especialidad_var).grid(
            row=5, column=1)

        ttk.Label(self, text="Diagnostico:").grid(row=6, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.diagnostico_var).grid(
            row=6, column=1)

        ttk.Label(self, text="Fecha Emision:").grid(
            row=7, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.fecha_emision_var).grid(
            row=7, column=1)

        ttk.Label(self, text="Medicamento:").grid(row=8, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.medicamento_var).grid(
            row=8, column=1)

        ttk.Label(self, text="Laboratorio:").grid(row=9, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.laboratorio_var).grid(
            row=9, column=1)

        ttk.Label(self, text="Mg:").grid(row=10, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.mg_var).grid(row=10, column=1)

        ttk.Label(self, text="Fecha Elaboracion:").grid(
            row=11, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.fecha_elab_var).grid(
            row=11, column=1)

        ttk.Label(self, text="Fecha Vencimiento:").grid(
            row=12, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.fecha_venc_var).grid(
            row=12, column=1)

        # Botones
        ttk.Button(self, text="Crear Paciente", command=self.crear_paciente).grid(
            row=13, column=0, pady=10)
        ttk.Button(self, text="Crear Medico", command=self.crear_medico).grid(
            row=13, column=1, pady=10)
        ttk.Button(self, text="Crear Receta", command=self.crear_receta).grid(
            row=14, column=0, pady=10)
        ttk.Button(self, text="Crear Medicamento", command=self.crear_medicamento).grid(
            row=14, column=1, pady=10)

    def crear_paciente(self):
        paciente = Paciente(self.nombre_var.get(), self.apellido_var.get(
        ), self.rut_var.get(), self.edad_var.get(), self.direccion_var.get())
        self.insertar_paciente(paciente)

    def crear_medico(self):
        medico = Medico(self.nombre_var.get(), self.apellido_var.get(
        ), self.direccion_var.get(), self.especialidad_var.get())
        self.insertar_medico(medico)

    def crear_receta(self):
        receta = RecetaMedica(self.nombre_var.get(
        ), self.diagnostico_var.get(), self.fecha_emision_var.get())
        self.insertar_receta(receta)

    def crear_medicamento(self):
        medicamento = Medicamento(self.medicamento_var.get(), self.laboratorio_var.get(
        ), self.mg_var.get(), self.fecha_elab_var.get(), self.fecha_venc_var.get())
        self.insertar_medicamento(medicamento)

    def insertar_paciente(self, paciente):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Pacientes (nombre, apellido, rut, edad, direccion)
                          VALUES (?, ?, ?, ?, ?)''',
                       (paciente.nombre, paciente.apellido, paciente.rut, paciente.edad, paciente.direccion))
        conn.commit()
        conn.close()
        print("Paciente insertado en la base de datos")

    def insertar_medico(self, medico):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Medicos (nombre, apellido, direccion, especialidad)
                          VALUES (?, ?, ?, ?)''',
                       (medico.nombre, medico.apellido, medico.direccion, medico.especialidad))
        conn.commit()
        conn.close()
        print("Medico insertado en la base de datos")

    def insertar_receta(self, receta):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Recetas (nombre_medico, diagnostico, fecha_emision)
                          VALUES (?, ?, ?)''',
                       (receta.nombreMedico, receta.diagnostico, receta.fechaEmision))
        conn.commit()
        conn.close()
        print("Receta insertada en la base de datos")

    def insertar_medicamento(self, medicamento):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Medicamentos (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento)
                          VALUES (?, ?, ?, ?, ?)''',
                       (medicamento.nombre, medicamento.laboratorio, medicamento.mg, medicamento.fecha_elaboracion, medicamento.fecha_vencimiento))
        conn.commit()
        conn.close()
        print("Medicamento insertado en la base de datos")


# Configurar la base de datos
setup_database()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = Formulario()
    app.mainloop()
