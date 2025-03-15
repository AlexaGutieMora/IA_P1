# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:18:51 2025

@author: k
"""

############ LISTAS ################
lista_numeros = ["tres", "dos", "cinco", "cuatro", "uno"] #Creación de una lista
print(lista_numeros[0]) #Imprime el elemento que se encuentra en la posición cero de la lista

lista_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(lista_colores[-2]) #accede a la penúltima posición
print(lista_colores)

del(lista_colores[2]) #elimina el elemento de la posición marcada de la lista
del(lista_colores[-3]) 
print(lista_colores)

lista_colores.remove('azul') #elimina el elemento indicando su valor, no su posición
print(lista_colores)

#Pop sirve tiene dos funciones:
    #1. Elimina el último elemento de la lista 
    #2. Elimina y almacena elementos de la lista.
color_1 = lista_colores.pop(0)
color_2 = lista_colores.pop(1)
colores_eliminados = [color_1, color_2]
print("Los colores eliminados son: ", colores_eliminados)

lista_colores.append('celeste') #Inserta elementos a la lista ya creada
print(lista_colores)

lista_colores.insert(-1,'fucsia') #Inserta elementos a la lista con una posición deseada
print(lista_colores)

lista_colores.sort(reverse=True) #sort ordena la lista por orden ascendente, reverse=True lo hace descendente
print(lista_colores)

print(len(lista_colores)) #Determina la cantidad de elementos de la lista

#Creación de TUPLAS (son inmutables)
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[4])

#Convierte la lista en una tupla
lista_a_tupla = tuple(lista_colores)
print(type(lista_a_tupla)) #Imprime la clase 