import PySimpleGUI as sg
import json
import string
import random


layoutGeneral = [[sg.Text('Bienvenido al juego.')], [sg.Button('Jugar'), sg.Button('Configurar')]]
ventanaGeneral = sg.Window('Sopa de letras').Layout(layoutGeneral)

while True:
	event, values = ventanaGeneral.Read()
	if event == None:
		exit(0)
	elif event == 'Jugar':
		try:
			archCol = open('coloresElegidos.json', "r")
			archPal = open('config.json', "r")
			archConfigMisc = open('configMisc.json', "r")
			listaAyuda = json.load(archConfigMisc)
			listaPal = json.load(archPal)
		except:
			sg.Popup('No se realizó ninguna configuración previa.')
			import configColores
			break
		else:
			break
	elif event == 'Configurar':
		archCol = open('coloresElegidos.json', "r")
		archPal = open('config.json', "r")
		archConfigMisc = open('configMisc.json', "r")
		listaAyuda = json.load(archConfigMisc)
		listaPal = json.load(archPal)
		import configColores
		break

window_background_color = listaAyuda[0]['LookAndFeel']

def MayusMinus(opcion):
	
	if opcion == 'Mayúsculas':
		return string.ascii_uppercase
	else:
		return string.ascii_lowercase

def crearFrameHorizontal(listaLetra,maxLong,tamLista, fuente):
	frame_layout=[]
	cont=0
	largoAux=maxLong+5
	for i in range(0,tamLista):
		fila=[]
		cantRandom=largoAux-len(listaLetra[i])
		numAux=0
		numAux=random.randint(1,cantRandom)
		for y in range(1,numAux + 1):
			boton=sg.Button(random.choice(MayusMinus(listaAyuda[0]['MayusMinus'])),key=str(cont), size=(5,2),button_color=('white','darkblue'), font=(fuente))
			fila.append(boton)
			cont=cont+1
		for z in listaLetra[i]:
			fila.append(sg.Button(z,key=str(cont), size=(5,2),button_color=('white','darkblue'),  font=(fuente)))
			cont=cont+1
		cantRest=cantRandom-numAux
		for w in range(1,cantRest+1):
			fila.append(sg.Button(random.choice(MayusMinus(listaAyuda[0]['MayusMinus'])),key=str(cont), size=(5,2),button_color=('white','darkblue'),  font=(fuente)))
			cont=cont+1
		frame_layout.append(fila)
		fila=[]
		for h in range(0,largoAux):
			fila.append(sg.Button(random.choice(MayusMinus(listaAyuda[0]['MayusMinus'])),key=str(cont), size=(5,2),button_color=('white','darkblue'),  font=(fuente)))
			cont=cont+1
		frame_layout.append(fila)
	return frame_layout




def crearFrameVertical(palabra_columna,palabra_fila, cantPalabras, maxLong, fuente):
		cantidad_total_filas=maxLong+2
		cantidad_total_columnas=cantPalabras*2
		lista_final=[]
		posicion=0
		keyAux=0
		for fila in range(cantidad_total_filas):
			fila_actual=[]
			for columna in range(cantidad_total_filas):
				if columna in palabra_columna.keys():
						if palabra_fila[palabra_columna[columna]] <= fila:
								posicion=fila-palabra_fila[palabra_columna[columna]]
								fila_actual.append(sg.Button(palabra_columna[columna][posicion],key=str(keyAux), size=(5,2),button_color=('white','darkblue'), font=(fuente)) if len(palabra_columna[columna])-1 >= posicion  else sg.Button(random.choice(MayusMinus(listaAyuda[0]['MayusMinus'])),key=str(keyAux), size=(5,2),button_color=('white','darkblue'), font=(fuente)))
								keyAux=keyAux+1
						else:
								fila_actual.append(sg.Button(random.choice(MayusMinus(listaAyuda[0]['MayusMinus'])),key=str(keyAux), size=(5,2),button_color=('white','darkblue'), font=(fuente)))
								keyAux=keyAux+1
				else:
					fila_actual.append(sg.Button(random.choice(MayusMinus(listaAyuda[0]['MayusMinus'])),key=str(keyAux), size=(5,2),button_color=('white','darkblue'),  font=(fuente)))
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
	if listaAyuda[0]['MayusMinus'] == 'Mayúsculas':
		palabraSplit = list(map(lambda x: x.upper(), palabraSplit))
		print(palabraSplit)
		listaLetra.append(palabraSplit)
	else:
		listaLetra.append(palabraSplit)

palabra_columna={}
palabra_fila={}
num_fila=0
for i in listaAux1:
	if listaAyuda[0]['MayusMinus'] == 'Mayúsculas':
		palabra_fila[i.upper()]=num_fila
	else:
		palabra_fila[i]=num_fila
	#num_fila=num_fila+2
num_columna=0
for z in listaAux1:
	if listaAyuda[0]['MayusMinus'] == 'Mayúsculas':
		palabra_columna[num_columna]=z.upper()
	else:
		palabra_columna[num_columna]=z
	num_columna=num_columna+2


	


listaColores= json.load(archCol)
lista_botones_col = []
for elem in listaColores:
	if elem['Tipo'] == 'NN':
		boton_aux1=sg.Button('Sustantivo', button_color=('black', elem['Color']))
		lista_botones_col.append(boton_aux1)
	elif elem['Tipo'] == 'JJ':
		boton_aux2=sg.Button('Adjetivo', button_color=('black', elem['Color']))
		lista_botones_col.append(boton_aux2)
	else:
		boton_aux3=sg.Button('Verbo', button_color=('black', elem['Color']))
		lista_botones_col.append(boton_aux3)

boton_aux=sg.Button('Confirmar')
lista_botones_col.append(boton_aux)
if listaAyuda[0]['Ayuda'] != 'No':
	boton_aux=sg.Button('Mostrar Ayuda')
	lista_botones_col.append(boton_aux)
boton_aux=sg.Button('Salir')
lista_botones_col.append(boton_aux)
boton_aux=sg.Button('Mostrar Ayuda')

listaFin=[]
lista_Keys=[]

if listaAyuda[0]['Orientación'] == 'Horizontal':
	layout=crearFrameHorizontal(listaLetra,maxLong,tamLista, listaAyuda[0]['Fuente'])
else:
	layout= crearFrameVertical(palabra_columna,palabra_fila, tamLista, maxLong, listaAyuda[0]['Fuente'])

layout.append(lista_botones_col)		

sg.ChangeLookAndFeel(window_background_color)
ventana= sg.Window('Prueba').Layout(layout)
colorBoton=''
tipoPal=''
contJuego=0
while True:
	event, values = ventana.Read()
	if event is None or event == 'Salir':
		break
	elif event == 'Confirmar':
		palabra=''
		for tupla in listaFin:
			palabra=palabra+tupla[0]
		palabra=palabra.lower()
		ok=True
		if palabra in listaAux1:
			for elem in listaPal:
				if elem['Palabra'] == palabra and tipoPal == elem['Tipo']:
					sg.Popup('Palabra correcta')
					listaFin=[]
					lista_Keys=[]
					ok=True
					contJuego+=1
					if contJuego == tamLista:
						sg.Popup('Ganaste! Felicitaciones!')
						exit(0)
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
	elif event == 'Mostrar Ayuda':
		listaUsoAyuda= []
		if listaAyuda[0]['Ayuda'] == 'Solo Definicion':
			for elem in listaPal:
				listaUsoAyuda.append(elem['Definicion'])
		elif listaAyuda[0]['Ayuda'] == 'Solo Palabras':
			for elem in listaPal:
				listaUsoAyuda.append(elem['Palabra'])
		else:
			for elem in listaPal:
				strAyuda = elem['Palabra'] + ': ' + elem['Definicion']
				listaUsoAyuda.append(strAyuda)
		
		layoutAyuda = [[sg.Listbox(values=listaUsoAyuda, size=(80,20))]]
		ventanaAyuda = sg.Window('Ayuda').Layout(layoutAyuda)
		
		while True:
			event, values = ventanaAyuda.Read()
			if event is None:
				break
			
			
	else:
		ventana.FindElement(event).Update(button_color=('black', colorBoton))
		auxLetra = (ventana.FindElement(event).ButtonText, event)
		if auxLetra not in listaFin:
			listaFin.append(auxLetra)
		else: 
			for tupla in listaFin:
				if event == tupla[1]:
					ventana.FindElement(event).Update(button_color=('white', 'darkblue'))
					listaFin.pop(listaFin.index(tupla))

		
		
