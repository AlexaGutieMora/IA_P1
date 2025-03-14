# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:14:30 2025

@author: k
"""

################## CAPÍTULO 2: VARIABLES
text = "Hola, este es un ejemplo de variable"
print(text)

numero_1 = 1
numero_2 = 7
sumatoria = numero_1 + numero_2
print(sumatoria)

vartext_1 = 'Ejemplo comillas simples'
vartext_2 = "Ejemplo comillas dobles"

concatenar = "Soy" + " Alexa."
print(concatenar)

string_1 = "Soy"
string_2 = " Alexa."
cadena = string_1 + string_2
print(cadena)

palabra_1 = "Soy"
print(palabra_1 + " Alexa.")

nombre = "Alexa"
apellido_1 = "Gutierrez"
apellido_2 = "Morales"
nombre_completo  = nombre + " " + apellido_1 + " " + apellido_2 
print(nombre_completo)

titulo = "alexa gutierrez morales".title()
print(titulo)

minusculas = "ALeXa GuTIERReZ MoRAlES".lower()
print(minusculas)

mayusculas = "ALeXa GuTIERReZ MoRAlES".upper()
print(mayusculas)

print("-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.")




########################### cap 10
lista_numeros = ["tres", "dos", "cinco", "cuatro", "uno"]
print(lista_numeros[0])

lista_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(lista_colores[-2]) #accede a la penúltima posición
print(lista_colores)

del(lista_colores[1]) #elimina ese elemento de la lista
del(lista_colores[-3])
print(lista_colores)

lista_colores.remove('azul')
print(lista_colores)

color_1 = lista_colores(0).pop
color_2 = lista_colores(1).pop
colores_eliminados = [color_1, color_2]
print("Los colores eliminados son: " colores_eliminados)

lista_colores.append('celeste')
print(lista_colores)

lista_colores.insert(-1'fucsia')
print(lista_colores)

lista_colores.sort(reverse=True)
print(lista_colores)

print(len(lista_colores))

#######tuplas
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[4])

    





