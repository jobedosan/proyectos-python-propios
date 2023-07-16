#Objetivo
'''
Crear un programa que nos dibuje las combinaciones de las fichas de domino.
'''

#Tareas
# 1. Crear un ciclo for que nos dará el número de la izquierda en una ficha
# 2. Crear un ciclo for anidado que nos dará el número de la derecha en una ficha
# 3. Organizar un string que nos imprima las combinaciones de fichas
# 4. Agregar un parámetro end en el string para separar las impresiones por espacios
# 5. Utilizar un print para crear un salto de línea al culminar cada ciclo for no anidado

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()