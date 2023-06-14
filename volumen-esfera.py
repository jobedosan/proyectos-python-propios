#Tareas
# 1. Mostrar un letrero que diga al usuario qué es lo que hará el programa
# 2. Solicitar al usuario el radio de la esféra
# 3. Utilizar la fórmula para calcular el volumen de una esféra y guardar el resultado de una variable
# 4. Imprimir el resultado

print("Este programa determinará el volumen de una esféra a partir del radio introducido por el usuario\n")
radio = int(input("Introduzca el radio de la esféra: "))
volumen = str(radio**3*4*3.14/3)
print("El volumen de la esféra es de "+ volumen)