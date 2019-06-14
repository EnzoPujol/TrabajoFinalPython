import PySimpleGUI as sg
import json
import string

archCol = open('coloresElegidos.txt', "r")

archPal = open('config.json', "r")

listaPal = json.load(archPal)

print(listaPal)

listaAux1 = []
for i in listaPal:
	listaAux1.append(i['Palabra'])

print(listaAux1)

maxLong = max(map(lambda x: len(x), listaAux1))

print(maxLong)
