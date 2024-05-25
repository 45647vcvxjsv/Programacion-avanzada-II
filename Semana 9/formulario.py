import csv
import tkinter as tk
from tkinter import Label, Entry, Button, Frame

# Función para calcular el impuesto a pagar


def calcularImpuesto(ingreso, porcentaje_impuesto):
    try:
        ingreso = float(ingreso)
        porcentaje_impuesto = float(porcentaje_impuesto)
        impuesto_a_pagar = ingreso * (porcentaje_impuesto / 100)
        return round(impuesto_a_pagar, 2)
    except ValueError:
        return 0

# Función para recopilar datos ingresados y guardar en CSV


def guardarDatos():
    ingreso = entries['Ingreso'].get()
    impuesto = entries['Impuesto'].get()
    impuesto_a_pagar = calcularImpuesto(ingreso, impuesto)

    datos = {
        'Nombres': entries['Nombre'].get(),
        'Apellidos': entries['Apellido'].get(),
        'Rut': entries['Rut'].get(),
        'Sexo': entries['Sexo'].get(),
        'Ingreso': ingreso,
        'Impuesto': impuesto,
        'Impuesto a Pagar': impuesto_a_pagar
    }

    nombre_archivo = entry_nombre_archivo.get().strip()
    if nombre_archivo:
        nombre_csv = nombre_archivo + '.csv'
        with open(nombre_csv, 'w', newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=datos.keys())
            writer.writeheader()
            writer.writerow(datos)
        limpiarCampos()

# Función para limpiar campos después de recopilar datos


def limpiarCampos():
    for key in entries:
        entries[key].delete(0, tk.END)
    entry_nombre_archivo.delete(0, tk.END)


# Crear ventana principal
ventana = tk.Tk()
ventana.config(bg='lightgray')
ventana.title('Formulario de entrada de datos')

# Creación de los widgets
frame_datos = Frame(ventana, bg='AntiqueWhite1')
frame_datos.pack(pady=20, padx=20, fill='both', expand=True)

labels = ['Nombre', 'Apellido', 'Rut', 'Sexo', 'Ingreso', 'Impuesto']
entries = {}

for i, label_text in enumerate(labels):
    Label(frame_datos, text=label_text + ':', bg='AntiqueWhite1',
          fg='black').grid(row=i, column=0, pady=10, padx=10)
    entry = Entry(frame_datos, width=20, font=('Arial', 12))
    entry.grid(row=i, column=1)
    entries[label_text] = entry

Label(frame_datos, text='Nombre del archivo CSV:', bg='AntiqueWhite1',
      fg='black').grid(row=len(labels), column=0, pady=10, padx=10)
entry_nombre_archivo = Entry(frame_datos, width=20, font=('Arial', 12))
entry_nombre_archivo.grid(row=len(labels), column=1)

Button(frame_datos, text='Guardar', bg='AntiqueWhite1', fg='black', font=(
    'Arial', 12, 'bold'), command=guardarDatos).grid(row=len(labels)+1, columnspan=2, pady=20)

ventana.mainloop()
