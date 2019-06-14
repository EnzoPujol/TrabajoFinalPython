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
	for i in range(0,tamLista):
		fila=[]
		cantRandom=maxLong-len(listaLetra[i])
		for x in range(1,len(listaLetra)):
			numAux=0
			print('entra')
			if(cantRandom>0):
				numAux=random.randint(1,cantRandom)
				print(numAux)
				for y in range(1,numAux):
					print('entra')
					boton=sg.Button(random.choice(string.ascii_lowercase),key=str(cont))
					fila.append(boton)
					cont=cont+1
			for z in listaLetra[i]:
				fila.append(sg.Button(z,key=str(cont)))
				cont=cont+1
			cantRest=cantRandom-numAux
			for w in range(1,cantRest):
				print('entra')
				fila.append(sg.Button(random.choice(string.ascii_lowercase),key=str(cont)))
				cont=cont+1
		frame_layout.append(fila)
	return frame_layout
	

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
ventana= sg.Window('Prueba').Layout(layout)
while True:
	event, values = ventana.Read()
	if event== None:
		break
	else:
		print (event)
