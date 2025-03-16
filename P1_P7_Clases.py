# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 22:42:41 2025

@author: k
"""

############### CLASES #########################
class Usuario: #Crea una clase de nombre Usuario
	def __init__(self, nombre): #Init se usa para establecer valores iniciales a los objetos
		self.nombre = nombre #Self se utiliza como un puntero (this) o sea se refiere a sí mismo
	def imprime_datos(self): #Función que imprimirá el nombre del usuario
		print('Nombre:', self.nombre) 

usuario_1 = Usuario('Giovanna')#Crea una variable de la clase Usurario y le asigna el argumento 

usuario_1.nombre = 'Scarlett' #Cambia el valor de la clave

usuario_1.imprime_datos() #Llama a la función de imprimir de la clase

class UsuariosPremium(Usuario): #Subclase que hereda las propiedades de la clase padre (herencia)
	pass #Hace vacía a la clase 

def funcion1():
	global num1 #Declara a la variable num1 como global y permite que se pueda acceder a ella tanto dentro como fuera de la clase
	num1 = 10
funcion1()
print(num1)    
