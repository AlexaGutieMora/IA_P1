# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 23:36:07 2025

@author: k
"""

##################### MODULOS #######################

import math #Importa el módulo math (librería)
area = lambda radio: (math.pi * radio * radio) #La función lambda se denomina "anónima" y sirve para reducir la sintaxis
print(area(2)) #Imprime el area dandole el parámetro del radio (2)

import datetime #Librería de fecha
fecha = datetime.datetime.now() #fecha exacta
print(fecha)

import re #Módulo de expresiones regulares, o sea secuencias de caracteres que forman un patrón de búsqueda
texto = "When the Pawn Hits the Conflicts He Thinks Like a King What He Knows Throws the Blows When He Goes to the Fight and He'll Win the Whole Thing 'fore He Enters the Ring There's No Body to Batter When Your Mind Is Your Might So When You Go Solo, You Hold Your Own Hand and Remember That Depth Is the Greatest of Heights and If You Know Where You Stand, Then You Know Where to Land and If You Fall It Won't Matter, Cuz You'll Know That You're Right"
busqueda = re.search("Pawn", texto) #buscará la cadena de caracteres dentro de la variable texto
busqueda_search = re.search("e", texto) #buscará la ubicación de la letra e
busqueda_findall = re.findall("e", texto) #buscará la ubicación de TODAS las letras e, aunque no se limita solo a letras (puede buscar parráfos, palabras...)
corte = re.split("i", texto) #parte la cadena de texto
reemplazar = re.sub(" ", "*", texto) #remplaza el primer argumento por el segundo
print(busqueda)
print(busqueda_search)
print(busqueda_findall) 
print(corte)
print(reemplazar)


variable = "Correcto." 
try: #Bloque de prueba
	print(variable)
except: #Permite trabajar con errores
	print("ERROR. VARIABLE NO DECLARADA")
