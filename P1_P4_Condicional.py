# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:22:44 2025

@author: k
"""

####################### CONDICIONALES #################
#CONDICIONAL IF
numero_1 = 20
numero_2 = 20
if numero_1 == numero_2: #Evalúa y hace la comparación
	print("Ambos numeros son iguales.")


color = "rojo"
if color != "rojo": #Se utiliza una negación
    print("El color NO es rojo.")
else:   #Si no se cumple el if, se ejecutará la siguiente instrucción
    print("El color es rojo")

print("\n")

edad = int(input("¿Cuál es tu edad?\n")) #Pregunta al usuario y acepta una variable, que será leída por el condicional
if edad <= 0:
	print("Nadie puede tener esa edad.")
elif edad >= 1 and edad <= 18: #Elif se usa para cuando hay múltiples condiciones if
	print("Eres menor de edad.")
elif edad >= 18 and edad <= 100:
	print("Eres mayor de edad.")
elif edad >=18 and edad <= 45:
    print("Eres un adulto.")
elif edad <100 and edad <= 120:
    print("Eres demasiado viejo.")
else:
	print('Edad no válida.')

print("\n")

colores = ('azul', 'verde', 'amarillo', 'rosado') #Creamos una tupla con ciertos colores 
color = input("Introduce un color, por favor: ") #Pregunta al usuario por un color
if color in colores[0]: #Evalúa si el color ingresado por el usuario se encuentra dentro de la posición marcada en la tupla
    print("Color azul admitido.")
elif color in colores[1]:
    print("Color verde admitido.")
elif color in colores[2]:
    print("Color amarillo admitido.")
elif color in colores[3]:
    print("Color rosado admitido.")
else: 
    print("Color no admitido.")
    
print("\n")

#CONDICIONAL WHILE    
y = 0 #Asigna el valor de la variable igual a cero
while y >= -100: #Mientras el valor de y sea mayor o igual a -100, el ciclo se repetirá
    print("El valor de y es: ", y) #Imprime el valor de y
    y -= 20 #Decrementa el valor de y 20 y repite el ciclo
print("\n")

#CONDICIONAL WHILE CON IF
x = 0 #Se le asigna el valor 0 a x
while x <= 30: #Se repetirá el ciclo mientras x sea igual o menor a 30
    x += 1 #x incrementará UNO
    if x == 4 or x == 6 or x == 10: #Si x tiene uno de esos valores, no se imprimirá el número sino el siguiente mensaje
        print("Se ha saltado el valor ", x, "de x")
        continue #continúa con el ciclo
    if x == 15: #cortará el valor de x cuando llegue a 15
        print("Se rompió la ejecución del bucle cuando x valía", x)
        break #Determina que son los únicos casos que puede haber
    print(x) #Imprime el valor de x
print("\n")

colores_for = ('rojo', 'azul', 'verde', 'amarillo') #Creación de una tupla de colores
for x in colores_for: #Iteración hasta completar la cantidad de elementos de la tupla
	print('El color es: ' + x + '.') #Imprime el color correspondiente de cada iteración
print("\n")
    
for y in range (7, 700, 100): #Se colocan los parámetros dentro del range, que serían inicialización (comenzará el conteo desde el número 7), luego el límite que tendrá (hasta 700) y por último el incremento que dará (de 100)
    print(y)