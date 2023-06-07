#Objetivo
'''
Crear un programa que cuente los caracteres del texto ingresado por el usuario, sin conta los espacios que puedan llegar a ingresarse, pues así no contamos los humanos. 
'''

#Tareas
# 1. Solicitar la información al usuario
# 2. Eliminar los espacios del texto ingresado por el usuario
# 3. Imprimir por consola la cantidad de caracteres del texto ingresado por el usuario

#Esta primera línea recibe el texto ingresado por el usuario
texto_ingresado = input("Ingresa el texto para decirte cuántos caracteres tiene")

#La siguiente línea elimina los espacios del texto ingresado por el usuario
texto_ingresado = texto_ingresado.replace(" ", "")

#La siguiente línea imprime por consola la cantidad de caracteres del texto ingresado por el usuario sin contar los espacios
print(len(texto_ingresado))