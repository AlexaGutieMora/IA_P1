# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:21:49 2025

@author: k
"""

#########################DICCIONARIOS###############################

automovil_1 = { #crea el diccionario que almacenará:
	'Categoría': 'Sedan', #Claves (key): Valores (value) 
	'Modelo': 'Kia Forte',
}

automovil_2 = {
	'Categoría': 'Hatchback',
	'Modelo': 'Fiat Argo',
}

print(automovil_1) #Imprime todo el diccionario 1
print('El modelo', automovil_2['Modelo'], 'es un coche tipo',automovil_2['Categoría']) #Imprime texto junto a los valores dentro de las claves del diccionario

automovil_1['Modelo'] = 'Volkswagen Jetta' #Cambia el valor de dicha clave en el diccionario 1

for x in automovil_1: #Se pueden usar los for para iterar dentro del diccionario
	print(x, '=', automovil_1[x] + '.')

print(len(automovil_2)) #Imprime la cantidad de claves del diccionario

automovil_1['Color'] = 'Rojo' #Agrega una clave y un valor al diccionario
print(automovil_1) #Muestra el diccionario actualizado

del(automovil_1) #Elimina TODO el diccionario 1
del(automovil_2['Modelo']) #Solo eliminará la clave y valor de Modelo
print(automovil_2)

