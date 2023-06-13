#Tareas
#Crear una variable inicializada en 0 que irá guardando la suma de los múltiplos
#Crear una lista vacía donde se irán guardando los múltiplos de 3 y 5 para mostrarlos por consola
#Crear un ciclo que llegue hasta 1000
#Crear una condicional para evaluar cuáles números en el rango de 0 a 1000 son múltiplos de 5 o 3
#Guardar la suma de los múltiplos en la variable y los múltiplos en la lista creados al inicio del programa

sum = 0
multiplos = []

for i in range(1000):
    if i % 5 == 0 or i % 3 == 0:
        sum += i
        multiplos.append(i)
print(multiplos, sum)