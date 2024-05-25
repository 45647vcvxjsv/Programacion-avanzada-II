from tkinter import Tk, Button, Entry, Label, PhotoImage, Frame
from PIL import Image 
import requests
import time 

class WeatherApp(Frame):
  def __init__(self, master):
    super().__init__(master)
    self.master = master
    self.master.title('')
    self.master.config(bg='white')
    self.master.minsize(height=300, width=500)
    self.master.geometry('500x300+180+80')

    self.create_widgets()

  def create_widgets(self):
    # Frames
    self.frame_top = Frame(self.master, bg='white', highlightbackground='deep pink', highlightthickness=2)
    self.frame_top.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)

    self.frame_temp = Frame(self.master, bg='pale green', highlightbackground='dark violet', highlightthickness=2)
    self.frame_temp.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
    self.frame_temp_max = Frame(self.master, bg='SeaGreen1', highlightbackground='dark violet', highlightthickness=2)
    self.frame_temp_max.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
    self.frame_temp_min = Frame(self.master, bg='PaleTurquoise1', highlightbackground='dark violet', highlightthickness=2)
    self.frame_temp_min.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

    self.frame_humidity = Frame(self.master, bg='cyan2', highlightbackground='dark violet', highlightthickness=2)
    self.frame_humidity.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
    self.frame_wind = Frame(self.master, bg='aquamarine', highlightbackground='dark violet', highlightthickness=2)
    self.frame_wind.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
    self.frame_pressure = Frame(self.master, bg='sky blue', highlightbackground='dark violet', highlightthickness=2)
    self.frame_pressure.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

    # Widgets
    self.gif = PhotoImage(file='buscar.gif')
    self.btn_search = Button(self.frame_top, image=self.gif, bg='red', bd=0, command=self.animation)
    self.btn_search.grid(row=0, column=0, padx=2, pady=2)

    self.entry_city = Entry(self.frame_top, font=('Comic Sans MS', 12), highlightbackground='DarkOrchid1', highlightcolor="green2", highlightthickness=2)
    self.entry_city.grid(row=0, column=1, padx=5)
    Label(self.frame_top, text='Buscar', fg='gray55', bg='white', font=('Comic Sans MS', 10)).grid(row=0, column=2, padx=5)
    self.label_warning = Label(self.frame_top, fg='red2', bg='white', font=('Comic Sans MS', 12))
    self.label_warning.grid(row=0, column=3, padx=5)
    self.label_location = Label(self.frame_top, fg='magenta', bg='white', font=('Arial', 12, 'bold'))
    self.label_location.grid(row=0, column=4, padx=5)

    self.temp_label = Label(self.frame_temp, bg='pale green', font=('Impact', 20))
    self.temp_label.pack(expand=True, side='right')
    self.temp_max_label = Label(self.frame_temp_max, bg='SeaGreen1', font=('Impact', 20))
    self.temp_max_label.pack(expand=True, side='right')
    self.temp_min_label = Label(self.frame_temp_min, bg='PaleTurquoise1', font=('Impact', 20))
    self.temp_min_label.pack(expand=True, side='right')

    self.humidity_label = Label(self.frame_humidity, bg='cyan2', font=('Impact', 20))
    self.humidity_label.pack(expand=True, side='right')
    self.wind_label = Label(self.frame_wind, bg='aquamarine', font=('Impact', 20))
    self.wind_label.pack(expand=True, side='right')
    self.pressure_label = Label(self.frame_pressure, bg='sky blue', font=('Impact', 20))
    self.pressure_label.pack(expand=True, side='right')

  def animation(self):
    # Aquí va el código de animación
    self.frame.config(highlightbackground='red')
    self.frame2.config(highlightbackground='red')
    self.frame3.config(highlightbackground='red')
    self.frame4.config(highlightbackground='red')
    self.frame5.config(highlightbackground='red')
    self.frame6.config(highlightbackground='red')
    self.frame7.config(highlightbackground='red')
    self.peticion_tiempo()
    pass

  def request_weather(self):
    # Aquí va la petición a la API del clima
    ciudad = self.ingresa_ciudad.get()

    API = 'http://api.openweathermap.org/data/2.5/weather?q={nombre_de_la_ciudad}&appid={tu_api_key}'

    try:
      json_datos = request.get(API).json()
      self.temp['text'] = str(int(json_datos['main']['temp']- 273.15)) +"ºC"
      self.temp_min['text'] = str(int(json_datos['main']['temp_min']- 273.15)) +"ºC"
      self.temp_max['text'] = str(int(json_datos['main']['temp_max']- 273.15)) +"ºC"
      self.presion['text'] = str(json_datos['main']['pressure']) + 'hPa'
      self.humedad['text'] = str(json_datos['main']['humidity']) + '%'
      self.viento['text'] = str(int(json_datos['wind']['speed'])*18/5) + 'kn/h'
      self.localiddad['text'] = json_datos['name'] + '-' + json_datos['sys']['country']
      
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

      pass

if __name__ == "__main__":
    ventana = Tk()
    app = WeatherApp(ventana)
    app.mainloop()
