#Objetivo
'''
Crear un programa que nos diga la cantidad de permutaciones posibles con una cantidad de notas ingresada por el usuario, en estas permutaciones no se permitirá la repetición de notas, como ocurre en el dodecafonismo. En este caso se utiliza la fórmula Pe=e! (e es la cantidad de elementos y e! es igual a el factorial del número de elementos, un factorial es el resultado de multiplicar un valor por sus números inferiores inmediatos de forma sucesiva (hasta el 1), por ejemplo 4! = 4 * * 3 * 2 * 1.
'''

#Tareas
# 1. Crear la variable que guardará el número ingresado por el usuario
# 2. Transformar el número ingresado por el usuario de string a int
# 3. Crear una advertencia en caso de que el usuario ingrese un número decimal, el número debe ser entero
# 4. Calcular el factorial del número ingresado por el usuario
# 5. Mostrar el factorial del número del usuario por pantalla

num = input("Ingresa un número para calcular el factorial (el número debe ser entero): ")

while num.find(",") != -1 or num.find(".") != -1:
    print("Ingresaste un número decimal, debes ingresar un número entero para calcular el factorial")
    num = input("Ingresa un nuevo número: ")

num = int(num)
fact = 1

for i in range(fact, num+1):
    fact *= i
    
print (f"El factorial de {num} es {fact}")