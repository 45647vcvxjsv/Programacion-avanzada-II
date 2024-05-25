import tkinter as tk
from tkinter import ttk
import csv


def calcular_impuesto(monto):
    impuesto = monto * 0.20
    return impuesto


class Campo(object):
    def __init__(self, padre, linea, etiqueta, tipo, valor, modo=False):
        self.padre = padre
        self.linea = linea
        self.etiqueta = etiqueta
        self.valor = tk.StringVar()
        self.etiqueta = tk.Label(padre, text=etiqueta)
        self.etiqueta.grid(column=0, row=linea)
        tipos = {'combobox': self.combobox,
                 'entry': self.entry}
        tipos[tipo](valor, modo)

    def entry(self, valor, modo=False):
        self.ent = tk.Entry(self.padre, textvariable=self.valor)
        self.valor.set(valor)
        self.ent.grid(column=1, row=self.linea, padx=10, pady=5, sticky='w')
        # Verificar si es campo de ingreso
        if self.etiqueta.cget("text") == "Ingreso":
            self.ent.bind("<FocusOut>", self.calcular_impuesto)

    def combobox(self, valor, modo=False):
        estado = 'readonly' if modo else 'normal'
        self.box = ttk.Combobox(self.padre,
                                textvariable=self.valor,
                                state=estado)
        self.box['values'] = valor
        self.box.current(0)  # Selecciona el primer elemento de la tupla.
        self.box.grid(column=1, row=self.linea, padx=10, pady=5, sticky='w')

    def calcular_impuesto(self, evento):
        try:
            monto = float(self.valor.get())
            impuesto_calculado = calcular_impuesto(monto)
            self.padre.form.impuesto_var.set(f"${impuesto_calculado:.2f}")
        except ValueError:
            pass  # Si el valor ingresado no es un número, simplemente no hace nada


class Formulario(object):
    def __init__(self, padre, campos):
        self.padre = padre
        self.campos = {}
        self.guardar = False
        self.impuesto_var = tk.StringVar()  # Variable para mostrar el impuesto calculado
        linea = 0
        for campo in campos:
            etiqueta, tipo, valor, modo = campo
            self.campos[etiqueta] = Campo(padre, linea,
                                          etiqueta, tipo, valor, modo)
            linea += 1
        self.campo_csv = Campo(
            padre, linea, "Nombre del archivo CSV", "entry", "", False)
        linea += 1
        self.btnacep = tk.Button(padre, text="Aceptar", command=self.aceptar)
        self.btnacep.grid(column=1, row=linea, sticky='w', padx=10, pady=10)
        self.lblimpuesto = tk.Label(padre, text="Impuesto Calculado:")
        self.lblimpuesto.grid(column=0, row=linea + 1,
                              sticky='e', padx=10, pady=5)
        self.lblimpuesto_valor = tk.Label(
            padre, textvariable=self.impuesto_var)
        self.lblimpuesto_valor.grid(
            column=1, row=linea + 1, sticky='w', padx=10, pady=5)

    def aceptar(self):
        self.guardar = True
        datos = {campo: self.campos[campo].valor.get()
                 for campo in self.campos}
        nombre_archivo = self.campo_csv.valor.get()
        if nombre_archivo:
            with open(nombre_archivo, 'w', newline='') as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerow(datos.keys())
                writer.writerow(datos.values())
        self.padre.destroy()


if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title("Formulario")
    form = Formulario(raiz, [
        ["Nombre", "entry", "", False],
        ["Apellido", "entry", "", False],
        ["RUT", "entry", "", False],
        ["Ingreso", "entry", "", False],
        ["Sexo", "combobox", ['Masculino', 'Femenino'], False]
    ])
    raiz.mainloop()
    if form.guardar:
        for campo in form.campos:
            print(campo, form.campos[campo].valor.get())
