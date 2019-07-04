import Adafruit_DHT
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import RPi.GPIO as GPIO
import time
import PySimpleGUI as sg
import json

class Temperatura:

    def __init__(self, pin=17, sensor=Adafruit_DHT.DHT11):
        self._sensor = sensor
        self._data_pin = pin

    def leer_datos(self):
      humedad, temperatura = Adafruit_DHT.read_retry(self._sensor, self._data_pin)
      return {'temperatura': temperatura, 'humedad': humedad}

class Microfono:

    def __init__(self, canal=22):
        self._canal = canal
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._canal, GPIO.IN)
        GPIO.setwarnings(False)
        GPIO.add_event_detect(self._canal, GPIO.RISING)

    def detectar(self,funcion,parametros,i=0):
        while i<1:
            if GPIO.event_detected(self._canal):
                print('lee2')
                funcion(**parametros)
                i=i+1

class Matriz:
    def __init__(self, numero_matrices=1, orientacion=0, rotacion=0, ancho=8, alto=8):
        self.font = [CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT]
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, width=ancho, height=alto, cascaded=numero_matrices, rotate=rotacion)

    def mostrar_mensaje(self, msg, delay=0.1, font=1):
        show_message(self.device, msg, fill="white",
                     font=proportional(self.font[font]),
                     scroll_delay=delay)
def acciones(temperaturas=[]):
    temp_data = temperatura.leer_datos()
    temp_formateada = 'Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(temp_data['temperatura'], temp_data['humedad'])
    matriz.mostrar_mensaje(temp_formateada, delay=0.08, font=2)
    temperaturas.append(temp_data['temperatura'])


matriz = Matriz()
microfono = Microfono()
temperatura = Temperatura()
arch=open('datos-oficinas.json', "w")
listaJson=[]

layout=[[sg.Text('Ingrese el nombre de la oficina:')],
        [sg.Input('', size=(20,5))],
        [sg.Listbox(values=[], size=(15,15), key='oficinas')],
        [sg.Button('Agregar Oficina'),sg.Button('Comenzar medicion') ,sg.Button('Salir')]

]

listaOficinas=[]
oficina={}
temperaturas=[]

window= sg.Window('Registro ambiental').Layout(layout)


while True:
    event, values = window.Read()
    if event== None or event=='Salir':
        break
    if event=='Agregar Oficina':
        listaOficinas.append(values[0])
        window.FindElement('oficinas').Update(listaOficinas)
        oficina['Oficina']=values[0]
    if event=='Comenzar medicion':
        microfono.detectar(acciones,dict(temperaturas=temperaturas))
        oficina['Temp']=temperaturas
        listaJson.append(oficina)

json.dump(listaJson, arch, ensure_ascii=False, indent=4)    
