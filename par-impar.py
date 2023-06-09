#Objetivo
'''
Crear un programa que diga si los números ingresados son pares, impares, decimales o enteros 
'''

#Tareas
# 1. Crear un letrero que diga para qué sirve el programa
# 2. Solicitar la información al usuario
# 3. Evaluar si el número es par o impar

#La siguiente línea es el título del programa
print("Este programa te dirá si el número que ingresas es par, impar, entero o decimal")

#Esta línea recibe el número ingresado por el usuario
num = int(input("Ingresa un número: "))

#La siguiente condicional evalúa si el resto al dividir el número ingresado por el usuario entre 2 es igual a 0, si es igual a cero imprime que el número es par, en caso contrario es un número impar.
if num % 2 != 0:
    print("El número", num,"es impar")
else:
    print("El número", num, "ingresado par")


