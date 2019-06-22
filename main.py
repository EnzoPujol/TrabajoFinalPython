import PySimpleGUI as sg
import json
import string
import random
#import configColores

#orientacion=configColores.orientacion()
#upperLower=configColores.upperLower()
window_background_color = 'Black'
archCol = open('coloresElegidos.json', "r")
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




def crearFrameVertical(palabra_columna,palabra_fila):
		cantidad_total_filas=10
		cantidad_total_columnas=10
		lista_final=[]
		posicion=0
		keyAux=0
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
								fila_actual.append(sg.Button(palabra_columna[columna][posicion],key=str(keyAux), size=(5,2),button_color=('white','darkblue')) if len(palabra_columna[columna])-1 >= posicion  else sg.Button(random.choice(string.ascii_lowercase),key=str(keyAux), size=(5,2),button_color=('white','darkblue')))
								keyAux=keyAux+1
						else:
								fila_actual.append(sg.Button(random.choice(string.ascii_lowercase),key=str(keyAux), size=(5,2),button_color=('white','darkblue')))
								keyAux=keyAux+1
				else:
					fila_actual.append(sg.Button(random.choice(string.ascii_lowercase),key=str(keyAux), size=(5,2),button_color=('white','darkblue')))
					keyAux=keyAux+1
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


	


listaColores= json.load(archCol)
lista_botones_col = []
for elem in listaColores:
	if elem['Tipo'] == 'NN':
		boton_aux1=sg.Button('Sustantivo', button_color=('white', elem['Color']))
		lista_botones_col.append(boton_aux1)
	elif elem['Tipo'] == 'JJ':
		boton_aux2=sg.Button('Adjetivo', button_color=('white', elem['Color']))
		lista_botones_col.append(boton_aux2)
	else:
		boton_aux3=sg.Button('Verbo', button_color=('white', elem['Color']))
		lista_botones_col.append(boton_aux3)


listaFin=[]
lista_Keys=[]
#layout= crearFrameVertical(palabra_columna,palabra_fila)
layout=crearFrameHorizontal(listaLetra,maxLong,tamLista)
layout.append(lista_botones_col)		
boton_aux=sg.Button('Confirmar')
lista_botones=[]
lista_botones.append(boton_aux)
boton_aux=sg.Button('Salir')
lista_botones.append(boton_aux)
layout.append(lista_botones)
sg.ChangeLookAndFeel(window_background_color)
ventana= sg.Window('Prueba').Layout(layout)
colorBoton=''
tipoPal=''
while True:
	event, values = ventana.Read()
	if event is None or event == 'Salir':
		break
	elif event == 'Confirmar':
		palabra=''
		for tupla in listaFin:
			palabra=palabra+tupla[0]
		print(palabra)
		ok=True
		if palabra in listaAux1:
			for elem in listaPal:
				if elem['Palabra'] == palabra and tipoPal == elem['Tipo']:
					sg.Popup('Palabra correcta')
					listaFin=[]
					lista_Keys=[]
					ok=True
					break
				else:
					ok=False
			if ok == False:
				sg.Popup('Palabra incorrecta')
				for tupla in listaFin:
					ventana.FindElement(tupla[1]).Update(button_color=('black', 'darkblue'))
				listaFin=[]
				lista_Keys=[]
				ok=True
		else:
			sg.Popup('Palabra incorrecta')
			for tupla in listaFin:
				ventana.FindElement(tupla[1]).Update(button_color=('black', 'darkblue'))
			listaFin=[]
			lista_Keys=[]
	elif event == 'Sustantivo':
		colorBoton=listaColores[0]['Color']
		tipoPal=listaColores[0]['Tipo']
	elif event == 'Adjetivo':
		colorBoton=listaColores[1]['Color']
		tipoPal=listaColores[1]['Tipo']
	elif event == 'Verbo':
		colorBoton=listaColores[2]['Color']	
		tipoPal=listaColores[2]['Tipo']	
	else:
		print(event)
		ventana.FindElement(event).Update(button_color=('black', colorBoton))
		auxLetra = (ventana.FindElement(event).ButtonText, event)
		if auxLetra not in listaFin:
			listaFin.append(auxLetra)
		else: 
			for tupla in listaFin:
				if event == tupla[1]:
					ventana.FindElement(event).Update(button_color=('black', 'darkblue'))
					listaFin.pop(listaFin.index(tupla))

		
		
