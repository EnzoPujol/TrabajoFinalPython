from pattern.es import tag
from pattern.web import Wiktionary
import PySimpleGUI as sg
import string
#Recordar hacer def para no ejecutar solo

def esValidaPattern (tag):
	
	aux = tag.split('')
	
	if aux[0] in string.ascii_uppercase:
		return True
	else:
		return False

diseñoPalabras = [[sg.Text('Ingrese las palabra a buscar: ')],
					[sg.In('', key='palabra')],
					[sg.Submit('Agregar')]]
					
ventanaPal = sg.Window('Palabras').Layout(diseñoPalabras)



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
		
		
		palTag = tag(values['palabra'])
		
		if strTipo == palTag[0][1]:
			
			#Usar la definición de Wiktionary si los dos coinciden en el tipo de palabra.
			
			
		elif strTipo =! palTag[0][1]:
		
			#Usar definición de Wiktionary y hacer reporte de la diferencia de pattern.
			archivoReporte = open('reporte.txt, "w"')
			archivoReporte.write('Wiktionary y pattern no coinciden en la definición de tipo de la sig. palabra: ', values[palabra])
		elif strTipo == None and esValidaPattern(palTag[0][1]):
		
			#Ponerle definición a la palabra. Guardar definición en archivo local.
			
			#diseñoDef = [[sg.Text('Parece ser que su palabra no es una conocida. Inserte una definición para la misma:')],
			#			[sg.Input(), sg.Submit('Agregar def.')]]
			
			#ventanaDef = sg.Window('Agregar definición').Layout(diseñoDef)
			
			#while True:
			#	evento, valores: ventanaDef.Read()
			#	
			#	if evento == 'Agregar def.':
			#		Desaparecer ventana anterior.
			#		Si existe el archivo de definiciones, modificarlo, y si no, crearlo.
			#		Agregar la definición nueva.
			#		sg.Popup('Definición agregada')	
			#		break
			#Agregar la palabra nueva a la lista de palabras de la sopa.
			
		else: #No se encuentra en ningun recurso
			archivoReporte = open('reporte.txt', "w")
			arhcivoReporte.write(values['palabra'] + ' no es una palabra válida para usar.')
		print(palTag)
		#Buscar la palabra en wiktionary junto con su tipo (adj, sus, verb.) done.
		#Con pattern.es buscar el tipo de la palabra. done.
		#Comparar valores de verdad de ambas busquedas
		#dependiendo de estos valores, actuar o elaborar reportes dependiendo al caso.
		
					


