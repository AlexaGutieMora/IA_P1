# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:47:10 2025

@author: k
"""

############### FUNCIONES ########################
def suma(numero1, numero2): #Crea una función llamada suma, la cual tendrá dos argumentos para ejecutarse
	print(numero1 + numero2) #Una vez llamada, imprimirá la suma de lo ingresado en los argumentos
suma(8, 7) #Se llama a la función suma con los argumentos respectivos para número 1 y número 2

#Uso de *args (argumentos arbitrarios)
def sumatoria(*args): #*args permite usar un número indeterminado de argumentos, lo cual es muy flexible
	resultado = args[0] + args[1] + args[1] #Se sumarán todos los argumentos que se ingresen al momento de llamar a la función
	print('La suma de los números es:', resultado)
sumatoria(1, 2, 3) #Se llama a la función junto con el número "x" de argumentos

#Para usar argumentos arbitrarios en diccionarios, usaremos **kwargs
def colores (**kwargs):
	print("Este es el color " + kwargs['color1'] + '.')
colores(color1='rojo')

