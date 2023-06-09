#Objetivo
'''
Crear un programa que cuente los caracteres del texto ingresado por el usuario, sin conta los espacios que puedan llegar a ingresarse, pues así no contamos los humanos. 
'''

#Tareas
# 1. Crear un letrero que diga para qué sirve el programa
# 2. Solicitar la información al usuario
# 3. Eliminar los espacios del texto ingresado por el usuario
# 4. Imprimir por consola la cantidad de caracteres del texto ingresado por el usuario

print("Este programa te dirá la cantidad de caracteres que tiene cualquier texto que le ingreses")

#Esta primera línea recibe el texto ingresado por el usuario
texto_ingresado = input("Ingresa un texto para saber cuántos caracteres tiene: ")

#La siguiente línea elimina los espacios del texto ingresado por el usuario
texto_ingresado = texto_ingresado.replace(" ", "")

#La siguiente línea imprime por consola la cantidad de caracteres del texto ingresado por el usuario sin contar los espacios
print(len(texto_ingresado))