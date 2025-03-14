# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:18:51 2025

@author: k
"""

########################### cap 10 LISTAS
lista_numeros = ["tres", "dos", "cinco", "cuatro", "uno"]
print(lista_numeros[0])

lista_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(lista_colores[-2]) #accede a la penúltima posición
print(lista_colores)

del(lista_colores[2]) #elimina ese elemento de la lista
del(lista_colores[-3])
print(lista_colores)

lista_colores.remove('azul')
print(lista_colores)

color_1 = lista_colores.pop(0)
color_2 = lista_colores.pop(1)
colores_eliminados = [color_1, color_2]
print("Los colores eliminados son: ", colores_eliminados)

lista_colores.append('celeste')
print(lista_colores)

lista_colores.insert(-1,'fucsia')
print(lista_colores)

lista_colores.sort(reverse=True)
print(lista_colores)

print(len(lista_colores))

#######tuplas
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[4])

lista = list(colores)
print(type(lista))