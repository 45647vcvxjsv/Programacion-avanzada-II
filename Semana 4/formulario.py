import tkinter as tk 

ventana = tk.Tk()

#frame = tkinter.frame(window)

def escuela_frontera():
  Nombre = Ingrese_su_nombre.get()
  Apellido = Ingrese_su_apellido.get()
  Rut = Ingrese_su_rut.get()
  Genero = Ingrese_su_genero.get()
  Telefono = Ingrese_su_telefono.get()

  print(f"Nombre: {Nombre}, Apellido: {Apellido}, Rut: {Rut}, Sexo: {Sexo}, Telefono: {Telefono}")

ventana.geometry("1280x720")
ventana.title("Cuestionario de consulta -Escuela Nueva Frontera")


etiqueta_nombre = tk.Label(ventana, text="Nombre: ")
etiqueta_nombre.pack(side=tk.LEFT, padx=5, pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_apellido = tk.Label(ventana, text="Apellido: ")
etiqueta_apellido.pack(side=tk.LEFT, padx=5, pady=5)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

etiqueta_rut = tk.Label(ventana, text="Rut: ")
etiqueta_rut.pack(side=tk.LEFT, padx=5, pady=5)
entrada_rut = tk.Entry(ventana)
entrada_rut.pack()

etiqueta_genero = tk.Label(ventana, text="Genero: ")
etiqueta_genero.pack(side=tk.LEFT, padx=5, pady=5)
genero = tk.StringVar()
genero.set("Masculino")
opciones_genero = ["Masculino", "Femenino"]
tk.OptionMenu(ventana, genero, *opciones_genero).pack()

etiqueta_telefono = tk.Label(ventana, text="Telefono: ")
etiqueta_telefono.pack(side=tk.LEFT, padx=5, pady=5)
entrada_telefono = tk.Entry(ventana)
entrada_telefono.pack()

tk.Button(ventana, text="Enviar", command=escuela_frontera).pack()
vista_formulario = tk.Label(ventana, text="Informacion de formulario", font=("Helvetica", 16, "bold"))
vista_formulario.pack()


ventana.mainloop()




