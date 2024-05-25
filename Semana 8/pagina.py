import reflex as rx

class state(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("probando")

# Crear una instancia de la clase App
app = rx.App()

# Agregar la página a la aplicación
app.add_page(index)

# Compilar la aplicación
#sapp.compile() 