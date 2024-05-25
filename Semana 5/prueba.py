from tkinter import Tk, Button, Entry, Label, PhotoImage, Frame
from PIL import Image
import requests
import time


class Ventana(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)

        self.click = True

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(2, weight=1)

        self.frame = Frame(self.master, bg='white',
                           highlightbackground='deep pink', highlightthickness=2)
        self.frame.grid(columnspan=3, row=0, sticky='nsew', padx=5, pady=5)

        self.frame2 = Frame(self.master, bg='pale green',
                            highlightbackground='dark violet', highlightthickness=2)
        self.frame2.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
        self.frame3 = Frame(self.master, bg='SeaGreen1',
                            highlightbackground='dark violet', highlightthickness=2)
        self.frame3.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)
        self.frame4 = Frame(self.master, bg='PaleTurquoise1',
                            highlightbackground='dark violet', highlightthickness=2)
        self.frame4.grid(column=2, row=1, sticky='nsew', padx=5, pady=5)

        self.frame5 = Frame(self.master, bg='cyan2',
                            highlightbackground='dark violet', highlightthickness=2)
        self.frame5.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
        self.frame6 = Frame(self.master, bg='aquamarine',
                            highlightbackground='dark violet', highlightthickness=2)
        self.frame6.grid(column=1, row=2, sticky='nsew', padx=5, pady=5)
        self.frame7 = Frame(self.master, bg='sky blue',
                            highlightbackground='dark violet', highlightthickness=2)
        self.frame7.grid(column=2, row=2, sticky='nsew', padx=5, pady=5)

        self.widgets()

    def animacion(self):
        self.frame.config(highlightbackground='red')
        self.frame2.config(highlightbackground='red')
        self.frame3.config(highlightbackground='red')
        self.frame4.config(highlightbackground='red')
        self.frame5.config(highlightbackground='red')
        self.frame6.config(highlightbackground='red')
        self.frame7.config(highlightbackground='red')
        self.peticion_tiempo()

        gif = Image.open('buscar.gif')
        frames = gif.n_frames

        if self.click == True:
            for i in range(1, frames):
                self.inicio = PhotoImage(
                    file='buscar.gif', format='gif -index %i' % (i))
                self.bt_inicio['image'] = self.inicio
                time.sleep(0.04)
                self.master.update()
                self.click = False

                if i + 1 == frames:
                    self.click = True

    def peticion_tiempo(self):
        ciudad = self.ingresa_ciudad.get()

        API = 'http://api.openweathermap.org/data/2.5/weather?q={nombre_de_la_ciudad}&appid={tu_api_key}'

        try:
            json_datos = requests.get(API).json()
            self.temp['text'] = str(
                int(json_datos['main']['temp'] - 273.15)) + "ºC"
            self.temp_min['text'] = str(
                int(json_datos['main']['temp_min'] - 273.15)) + "ºC"
            self.temp_max['text'] = str(
                int(json_datos['main']['temp_max'] - 273.15)) + "ºC"
            self.presion['text'] = str(json_datos['main']['pressure']) + 'hPa'
            self.humedad['text'] = str(json_datos['main']['humidity']) + '%'
            self.viento['text'] = str(
                int(json_datos['wind']['speed']) * 18 / 5) + 'kn/h'
            self.localiddad['text'] = json_datos['name'] + \
                '-' + json_datos['sys']['country']

        except:
            self.aviso['aviso'] = 'error'
            self.temp['text'] = '_'
            self.temp_min['text'] = '_'
            self.temp_max['text'] = '_'
            self.presion['text'] = '_'
            self.humedad['text'] = '_'
            self.viento['text'] = '_'
            self.master.update()
            time.sleep(1)
            self.aviso['text'] = ''
            self.localiddad['text'] = ''

    def widgets(self):
        self.inicio = PhotoImage(file='buscar.gif')
        self.imagen_temp = PhotoImage(file='temperature.png')
        self.imagen_temp_min = PhotoImage(file='temp_min.png')
        self.imagen_temp_max = PhotoImage(file='temp_max.png')
        self.imagen_humedad = PhotoImage(file='humedad.png')
        self.imagen_tiempo = PhotoImage(file='tiempo.png')
        self.imagen_presion = PhotoImage(file='presion.png')

        self.bt_inicio = Button(self.frame, image=self.inicio, bg='red', highlightthickness=0, activebackground='white',
                                bd=0, command=self.animacion)
        self.bt_inicio.grid(column=0, row=0, padx=2, pady=2)
        self.ingresa_ciudad = Entry(self.frame, font=('Comic Sans MS', 12), highlightbackground='DarkOrchid1',
                                    highlightcolor="green2", highlightthickness=2)
        self.ingresa_ciudad.grid(column=1, row=0)

        Label(self.frame, text='Buscar', fg='gray55', bg='white', font=('Comic Sans MS', 10)).grid(column=2, row=0,
                                                                                                   padx=5)
        self.aviso = Label(self.frame, fg='red2', bg='white',
                           font=('Comic Sans MS', 12))
        self.aviso.grid(column=3, row=0, padx=0)
