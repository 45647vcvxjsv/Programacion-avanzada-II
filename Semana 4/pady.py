import tkinter as tk

def escuela_frontera():
    Nombre = entrada_nombre.get()
    Apellido = entrada_apellido.get()
    Rut = entrada_rut.get()
    Genero = genero.get()
    Telefono = entrada_telefono.get()
    Comuna = entrada_comuna.get()

    print(f"Nombre: {Nombre}, Apellido: {Apellido}, Rut: {Rut}, Genero: {Genero}, Telefono: {Telefono}")

#def cargar_imagen():
    #imagen = tk.PhotoImage(file="/Users/luisalvarez/Downloads/POO/Programacion avanzada 2/Semana 4/duda.png")
    #etiqueta_imagen.config(image=imagen)
    #etiqueta_imagen.image = imagen 


ventana = tk.Tk()
ventana.configure(bg="#63C5DA")  


frame_principal = tk.Frame(ventana, bg="white")  
frame_principal.pack(padx=20, pady=20)


titulo = tk.Label(frame_principal, text="Consulta ciudadana ", font=("Helvetica", 18, "bold"), bg="#89CFF0")
titulo.grid(row=0, columnspan=2, pady=10)


etiqueta_nombre = tk.Label(frame_principal, text="Nombre (*): ", bg="#ffbf34")  
etiqueta_nombre.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_nombre = tk.Entry(frame_principal)
entrada_nombre.grid(row=1, column=1)

etiqueta_apellido = tk.Label(frame_principal, text="Apellido (*): ", bg="#ffbf34")  
etiqueta_apellido.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entrada_apellido = tk.Entry(frame_principal)
entrada_apellido.grid(row=2, column=1)

etiqueta_rut = tk.Label(frame_principal, text="Rut (*): ", bg="#ffbf34") 
etiqueta_rut.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entrada_rut = tk.Entry(frame_principal)
entrada_rut.grid(row=3, column=1)

etiqueta_genero = tk.Label(frame_principal, text="Genero (*): ", bg="#ffbf34")  
etiqueta_genero.grid(row=4, column=0, padx=5, pady=5, sticky="w")
genero = tk.StringVar()
genero.set("Masculino")
opciones_genero = ["Masculino", "Femenino"]
opciones_menu = tk.OptionMenu(frame_principal, genero, *opciones_genero)
opciones_menu.grid(row=4, column=1, padx=5, pady=5, sticky="w")

etiqueta_telefono = tk.Label(frame_principal, text="Telefono (*): ", bg="#ffbf34")  
etiqueta_telefono.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entrada_telefono = tk.Entry(frame_principal)
entrada_telefono.grid(row=5, column=1)

entrada_comuna = tk.Label(frame_principal, text="Comuna (*):", bg="#ffbf34")
entrada_comuna.grid(row=6, column=0, padx=5, pady=5, sticky="w")
entrada_comuna = tk.Entry(frame_principal)
entrada_comuna.grid(row=6, column=1)


frame_secundario = tk.Frame(ventana, bg="#30d5c8")  
frame_secundario.pack(padx=20, pady=20)

etiqueta_cuestionario = tk.Label(frame_secundario, text="Ud, estaria a favor de la construccion: ", bg="#ffbf34")  
etiqueta_cuestionario.grid(row=0, column=0, padx=5, pady=5, sticky="w")
Cuestionario = tk.StringVar()
Cuestionario.set("Si")
opciones_cuestionario = ['Si', 'No']
opciones_menu = tk.OptionMenu(frame_secundario, Cuestionario, *opciones_cuestionario)
opciones_menu.grid(row=0, column=1)


boton_enviar = tk.Button(frame_secundario, text="Enviar", command=escuela_frontera)
boton_enviar.grid(row=1, column=0, columnspan=2, pady=10)



ventana.mainloop()
