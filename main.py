import PySimpleGUI as sg
import json
import string
import random
#import configColores

#orientacion=configColores.orientacion()
#upperLower=configColores.upperLower()
window_background_color = 'Black'
archCol = open('coloresElegidos.txt', "r")
archPal = open('config.json', "r")
listaPal = json.load(archPal)


def crearFrameHorizontal(listaLetra,maxLong,tamLista):
	frame_layout=[]
	cont=0
	largoAux=maxLong+5
	for i in range(0,tamLista):
		fila=[]
		cantRandom=largoAux-len(listaLetra[i])
		numAux=0
		numAux=random.randint(1,cantRandom)
		for y in range(1,numAux + 1):
			boton=sg.Button(random.choice(string.ascii_lowercase),key=str(cont), size=(5,2),button_color=('white','darkblue'))
			fila.append(boton)
			cont=cont+1
		for z in listaLetra[i]:
			fila.append(sg.Button(z,key=str(cont), size=(5,2),button_color=('white','darkblue')))
			cont=cont+1
		cantRest=cantRandom-numAux
		for w in range(1,cantRest+1):
			fila.append(sg.Button(random.choice(string.ascii_lowercase),key=str(cont), size=(5,2),button_color=('white','darkblue')))
			cont=cont+1
		frame_layout.append(fila)
		fila=[]
		for h in range(0,largoAux):
			fila.append(sg.Button(random.choice(string.ascii_lowercase),key=str(cont), size=(5,2),button_color=('white','darkblue')))
			cont=cont+1
		frame_layout.append(fila)
	return frame_layout

def boton(nombre,tam=(5,2),color=('white','green'),clave=''):
    if clave != '':
        return sg.Button(nombre, size=tam ,button_color=color,key=clave)
    else:
        return sg.Button(nombre, size=tam ,button_color=color)

def crearFrameVertical(palabra_columna,palabra_fila):
		cantidad_total_filas=10
		cantidad_total_columnas=10
		lista_final=[]
		posicion=0
		for fila in range(cantidad_total_filas):
			fila_actual=[]
			for columna in range(cantidad_total_filas):
				#evaluo si es que estoy en una columna de donde pertenece la palabra, caso contrario agrego el boton con el numero, en su caso es una letra random
				if columna in palabra_columna.keys():
					#evaluo si es que estoy en la fila correspondiente de donde puedo arrancar, caso contrario agrego el boton del numero, en su caso es una letra random
						if palabra_fila[palabra_columna[columna]] <= fila:
								#posicion va a ser la variable la cual indique por cual letra esta yendo por fila
								posicion=fila-palabra_fila[palabra_columna[columna]]
								# aca agrego el boton con la letra correspondiente o un numero, que vendria a ser una letra aleatoria en su caso
								fila_actual.append(boton(palabra_columna[columna][posicion],color=('white','red')) if len(palabra_columna[columna])-1 >= posicion  else boton(random.choice(string.ascii_lowercase)))
						else:
								fila_actual.append(boton(random.choice(string.ascii_lowercase)))
				else:
					fila_actual.append(boton(random.choice(string.ascii_lowercase)))
			lista_final.append(fila_actual.copy()) 
		return lista_final



listaAux1 = []
for i in listaPal:
	listaAux1.append(i['Palabra'])

maxLong = max(map(lambda x: len(x), listaAux1))
tamLista=len(listaPal)

listaLetra= []

for i in listaAux1:
	palabraSplit=list(i)
	listaLetra.append(palabraSplit)

palabra_columna={}
palabra_fila={}
num_fila=0
for i in listaAux1:
	palabra_fila[i]=num_fila
	num_fila=num_fila+2
num_columna=0
for z in listaAux1:
	palabra_columna[num_columna]=z
	num_columna=num_columna+2



sopa=crearFrameHorizontal(listaLetra,maxLong,tamLista)
boton_aux=sg.Button('Confirmar')
lista_botones=[]
lista_botones.append(boton_aux)
boton_aux=sg.Button('salir')
lista_botones.append(boton_aux)
sopa.append(lista_botones)
listaFin=[]
lista_Keys=[]
layout=sopa	
#layout =  crearFrameVertical(palabra_columna,palabra_fila)
sg.ChangeLookAndFeel(window_background_color)
ventana= sg.Window('Prueba').Layout(layout)
while True:
	event, values = ventana.Read()
	if event== None or 'salir':
		break
	if event=='Confirmar':
		palabra=''
		palabra=palabra.join(listaFin)
		print(palabra)
		if palabra in listaAux1:
			sg.Popup('Palabra correcta')
			listaFin=[]
			lista_Keys=[]
		else:
			sg.Popup('Palabra incorrecta')
			listaFin=[]
			lista_Keys=[]
	else:
		ventana.FindElement(event).Update(button_color=('white', 'green'))
		listaFin.append(ventana.FindElement(event).ButtonText)
		if event in lista_Keys:
			ventana.FindElement(event).Update(button_color=('white', 'darkblue'))
			print(ventana.FindElement(event).ButtonText)
			listaFin.remove(ventana.FindElement(event).ButtonText)
			print(listaFin)
		else:
			lista_Keys.append(event)
		
		
