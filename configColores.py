# -*- coding: utf-8 -*-

from pattern.es import tag
from pattern.web import Wiktionary
import PySimpleGUI as sg
import string
import json
import os

dic_configMisc={}


def ayuda():
	diseñoAyuda = [[sg.Text('¿Desea ayuda?')],
					[sg.Button('Solo Definicion'),sg.Button('Solo Palabras'),sg.Button('Definicion y Palabras'), sg.Button('No')]]
	
	ventanaAyuda = sg.Window('Ayuda').Layout(diseñoAyuda)
	
	while True:
		event, values = ventanaAyuda.Read()
		if event is None:
			break
		else:
			return event
def orientacion():
	diseñoOrient = [[sg.Text('Elegir orientación de las palabras:')], [sg.Button('Horizontal'), sg.Button('Vertical')]]
	ventanaOrient = sg.Window('Orientación').Layout(diseñoOrient)
	
	while True:
		event, values = ventanaOrient.Read()
		if event is None:
			break
		else:
			return event
def upperLower():
	diseñoUL = [[sg.Text('Mayúsculas o minúsculas:')], [sg.Button('Mayúsculas'), sg.Button('Minúsculas')]]
	ventanaUL = sg.Window('Orientación').Layout(diseñoUL)
	
	while True:
		event, values = ventanaUL.Read()
		if event is None:
			break
		else:
			return event
			
def fuente():
	fuentes = ['Helvetica', 'Verdana', 'Times', 'Fixedsys', 'Arial', 'Courier', 'Comic']
	
	layoutFuente = [[sg.Text('Elija una de las fuentes disponibles:')],
					[sg.In('', key='fuente')],[sg.Listbox(values=fuentes, size=(15,15), key='fuentes')],
					[sg.Button('Confirmar')]]
					
	ventanaFuente = sg.Window('Elegir fuente').Layout(layoutFuente)
	
	while True:
		event, values = ventanaFuente.Read()
		if event is None:
			break
		if event == 'Confirmar':
			fuente = values['fuente'].lower()
			fuente = fuente.capitalize()
			if fuente in fuentes:
				return fuente
			else:
				sg.Popup('Por favor, elija una de las fuentes disponibles.')	
def cantTipos():
	layoutCant = [[sg.Text('Ingrese cantidad de sustantivos, adjetivos y verbos en orden, separados por coma:')], [sg.Input('', size=(5,5))], [sg.Button('Confirmar')]]
	ventanaCant = sg.Window('Cantidad de palabras').Layout(layoutCant)
	while True:
		event, values = ventanaCant.Read()
		if event == None:
			break
		elif event == 'Confirmar':
			return values[0].split(',')
			break

	
#Recordar hacer def para no ejecutar solo
archivoJson=open('config.json','w+')

diseñoPalabras = [[sg.Text('Ingrese las palabra a buscar: ')],
					[sg.In('', key='palabra')],
					[sg.Submit('Agregar'), sg.Button('Siguiente')]]
					
ventanaPal = sg.Window('Palabras').Layout(diseñoPalabras)

listaJSONPal = []
strDef = ''
listaCantPal = cantTipos()
print(listaCantPal)
contSustantivos, contAdjetivos, contVerbos = 0,0,0
while True:
	event, values = ventanaPal.Read()
	if event is None:
		exit(0)
	elif event == 'Agregar':
		w = Wiktionary(language="es")
		p = w.search(values['palabra'], type='search', start=1, count=10)
		strTipo = ''
		try:
			artic = p.plaintext().split('\n')
			strNuevo = ' - '.join(artic)
			
			if 'Sustantivo' in strNuevo:
				strTipo = 'NN'
			elif 'Adjetivo' in strNuevo:
				strTipo = 'JJ'
			elif 'Verbo' in strNuevo:
				strTipo = 'VB'
		except AttributeError:
			sg.Popup('La palabra no existe.')
			strTipo = None
		finally:
			print(strTipo)
		
		strDef = strNuevo.split('- 1')
		strDef = strDef[1].split('2')
		if '-' in strDef[0]:
			strDef = strDef[0].split('-')
			strDef = strDef[0]
		else:
			strDef = strDef[0]
		
		
		palTag = tag(values['palabra'])
		
		if strTipo == palTag[0][1]:
			#Usar la definición de Wiktionary si los dos coinciden en el tipo de palabra.
			dic={}
			dic['Palabra']=values['palabra']
			dic['Definicion']=strDef
			dic['Tipo']=palTag[0][1]
			if strTipo == 'NN':
				if contSustantivos < int(listaCantPal[0]):
					listaJSONPal.append(dic)
					contSustantivos+=1
			if strTipo == 'JJ':
				if contAdjetivos < int(listaCantPal[1]):
					listaJSONPal.append(dic)
					contAdjetivos+=1
			if strTipo == 'VB':
				if contVerbos < int(listaCantPal[2]):
					listaJSONPal.append(dic)
					contVerbos+=1
			print(listaJSONPal)
		elif strTipo != palTag[0][1]:
			#Usar definición de Wiktionary y hacer reporte de la diferencia de pattern.
			dic={}
			dic['Palabra']=values['palabra']
			dic['Definicion']=strDef
			dic['Tipo']=palTag[0][1]
			if strTipo == 'NN':
				if contSustantivos < int(listaCantPal[0]):
					listaJSONPal.append(dic)
					contSustantivos+=1
			if strTipo == 'JJ':
				if contAdjetivos < int(listaCantPal[1]):
					listaJSONPal.append(dic)
					contAdjetivos+=1
			if strTipo == 'VB':
				if contVerbos < int(listaCantPal[2]):
					listaJSONPal.append(dic)
					contVerbos+=1
			archivoReporte = open('reporte.txt', "w")
			archivoReporte.write('Wiktionary y pattern no coinciden en la definición de tipo de la sig. palabra: '+values['palabra'])
		else:
			if(os.path.exists(reporte.txt)):
				archivoReporte = open('reporte.txt', 'r+')
			else:
				archivoReporte = open('reporte.txt','w+')
			arhcivoReporte.write(values['palabra'] + ' no es una palabra válida para usar.')
	elif event == 'Siguiente':
		break		

json.dump(listaJSONPal, archivoJson, ensure_ascii=False, indent=4)

coloresEN = ['yellow', 'red', 'blue', 'green', 'purple', 'light blue', 'orange', 'brown']
coloresES = ['amarillo', 'rojo', 'azul', 'verde', 'violeta', 'celeste', 'naranja', 'marrón']

diseñoColores = [[sg.Text('Ingrese los colores a utilizar:')],[sg.Text('(Elija color para sustantivo, adjetivo y verbo en orden.)')],
					[sg.In('', key='color')],[sg.Listbox(values=coloresES, size=(15,15), key='colores'), sg.Listbox(values=[], size=(15,15), key='colEleg')],
					[sg.Button('Agregar color'), sg.Button('Quitar color'), sg.Button('Confirmar')]]

ventanaColores = sg.Window('Elegir colores a usar').Layout(diseñoColores)

coloresEN = ['yellow', 'red', 'blue', 'green', 'purple', 'light blue', 'orange', 'brown']
coloresES = ['amarillo', 'rojo', 'azul', 'verde', 'violeta', 'celeste', 'naranja', 'marrón']


listaJson=[]
coloresElegidos = []
contCol = 0

while True:
	event, values = ventanaColores.Read()
	if event is None:
		break
	elif event == 'Agregar color':
		if values['color'] in coloresES and values['color'] not in coloresElegidos and contCol < 3: 
			coloresElegidos.append(values['color'])
			ventanaColores.FindElement('colEleg').Update(coloresElegidos)
			contCol +=1
		elif values['color'] not in coloresES:
			sg.Popup('Por favor, elija uno de los colores de la lista.')
		elif values['color'] in coloresElegidos:
			sg.Popup('El color ingresado ya se eligió previamente.')
		elif contCol == 3:
			sg.Popup('Máximo de colores alcanzado. Si quiere agregar otro, borre uno.')
	elif event == 'Quitar color':
		try:
			indiceCol = coloresElegidos.index(values['color'])	
		except ValueError:
			sg.Popup('La lista de colores elegidos está vacía.')	
		else:
			del coloresElegidos[indiceCol]
			contCol -=1
			ventanaColores.FindElement('colEleg').Update(coloresElegidos)
	elif event == 'Confirmar':
		try:
			colElegEnglish = []
			for i in coloresElegidos:
				indAux = coloresES.index(i)
				colElegEnglish.append(coloresEN[indAux])
			print(colElegEnglish)
			cont=0
			for x in colElegEnglish:
				dicColor = {}
				dicColor['Color'] = x
				if cont == 0:
					dicColor['Tipo'] = 'NN'
				elif cont == 1:
					dicColor['Tipo'] = 'JJ'
				else:
					dicColor['Tipo'] = 'VB'
				print(x)
				listaJson.append(dicColor)
				cont+=1
		except TypeError:
			sg.Popup('No eligió ningún color.')
		else:
			archivoColores = open('coloresElegidos.json', "w")
			json.dump(listaJson, archivoColores)	
			archivoColores.close()	
			print(listaJson)		
		break

dic_configMisc['Ayuda'] = ayuda()
dic_configMisc['Fuente'] = fuente()
dic_configMisc['Orientación'] = orientacion()
dic_configMisc['MayusMinus'] = upperLower()

archConfigMisc = open('configMisc.json', "w")
listaJSONMisc = []
listaJSONMisc.append(dic_configMisc)
json.dump(listaJSONMisc, archConfigMisc, ensure_ascii=False, indent=4)
