#Objetivo
'''
Crear un programa que diga si los números ingresados son pares, impares, decimales o enteros 
'''

#Tareas
# 1. Crear un letrero que diga para qué sirve el programa
# 2. Solicitar la información al usuario
# 3. Evaluar si el dato ingresado por el usuario tiene una coma o punto
# 4. Evaluar si el número es decimal o entero

#La siguiente línea es el título del programa
print("Este programa te dirá si el número que ingresas entero o decimal")

#Esta línea recibe el número ingresado por el usuario
num = input("Ingresa un número: ")

#La siguientes dos variables serán utilizadas en la validación, se encargan de buscar si hay una coma o punto en el número ingresado por el usuario
coma = num.find(",")
punto = num.find(".")

#La siguiente condicional ve en las variables coma y punto si el número ingresado tenía coma o punto, si lo tiene indica que es decimal y si no indica que es entero
if coma and  punto != -1:
    print("El número", num, "es un decimal")
else:
    print("El número", num, "es entero")