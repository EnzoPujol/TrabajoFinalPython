import PySimpleGUI as sg
import json
import string
import random
#import configColores

#orientacion=configColores.orientacion()
#upperLower=configColores.upperLower()

def crearFrameHorizontal(listaLetra,maxLong,tamLista):
	frame_layout=[]
	cont=0
	largoAux=maxLong+5
	for i in range(0,tamLista):
		fila=[]
		cantRandom=largoAux-len(listaLetra[i])
		numAux=0
		numAux=random.randint(1,cantRandom)
		print(numAux)
		for y in range(1,numAux + 1):
			boton=sg.Button(random.choice(string.ascii_lowercase),key=str(cont), size=(2,2))
			fila.append(boton)
			cont=cont+1
		for z in listaLetra[i]:
			fila.append(sg.Button(z,key=str(cont), size=(2,2)))
			cont=cont+1
		cantRest=cantRandom-numAux
		for w in range(1,cantRest+1):
			fila.append(sg.Button(random.choice(string.ascii_lowercase),key=str(cont), size=(2,2)))
			cont=cont+1
		frame_layout.append(fila)
	return frame_layout

def crearFrameVertical(frame_layout, maxLong):
	frame_vert = []
	largoAux=maxLong+5
	for j in range(0,largoAux):
			fila=[]
			frame_vert.append(fila)
	cont=0
	for i in frame_layout:
		for k in i:
			frame_vert[cont]=k
			cont+=1
		cont=0 
	return frame_vert

archCol = open('coloresElegidos.txt', "r")
archPal = open('config.json', "r")
listaPal = json.load(archPal)

listaAux1 = []
for i in listaPal:
	listaAux1.append(i['Palabra'])

maxLong = max(map(lambda x: len(x), listaAux1))
tamLista=len(listaPal)

listaLetra= []

for i in listaAux1:
	palabraSplit=list(i)
	listaLetra.append(palabraSplit)
print(listaLetra)


layout=crearFrameHorizontal(listaLetra,maxLong,tamLista)
layoutVert=crearFrameVertical(layout, maxLong)
print(layoutVert)

ventana= sg.Window('Prueba').Layout([layoutVert])
while True:
	event, values = ventana.Read()
	if event== None:
		break
	else:
		print (event)
