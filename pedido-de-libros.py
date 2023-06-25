#Objetivo
'''
Crear un programa que diga si los números ingresados son pares, impares, decimales o enteros 
'''
#Tareas
#Pedir al usuario el precio del libro a ordenar
#Evaluar si el número es entero o es decimal
#Pedir el descuento que le corresponde
#Pedir la cantidad de copias a ordenar
#Pedir el costo de envío que se le indicó al usuario
#Pedir el costo del envío de la primera copia
#Pedir el costo del envío del resto de copias
#Dar el total al usuario
LibroPrecio = input("Ingresa el precio del libro a ordenar: \n")

if LibroPrecio.find(",") == -1 and LibroPrecio.find(".") == -1:
    LibroPrecio = int(LibroPrecio)
else:
   LibroPrecio = float(LibroPrecio)
   
EnvioCopia1 = input("Ingrese el costo del envío para la primera copia: \n")
    
if EnvioCopia1.find(",") == -1 and EnvioCopia1.find(".") == -1:
    EnvioCopia1 = int(EnvioCopia1)
else:
   EnvioCopia1 = float(EnvioCopia1)
   
EnvioResto = input("Ingrese el costo del envío para las copias adicionales: \n")

if EnvioResto.find(",") == -1 and EnvioResto.find(".") == -1:
    EnvioResto = int(EnvioResto)
else:
   EnvioResto = float(EnvioResto)
   
LibroDescuento = int(input("Ingrese el descuento a aplicar al libro: \n"))

CantidadCopias = int(input("Ingrese la cantidad de copias que encargará: \n"))-1 

CostoPrimeraCopia = LibroPrecio - (LibroDescuento * LibroPrecio/100)
CostoPrimeraCopia_total= round(CostoPrimeraCopia, 2) + round(EnvioCopia1, 2)

CostoRestoCopias = CostoPrimeraCopia
CostoRestoCopias = CostoRestoCopias + EnvioResto
CostoRestoCopias *= CantidadCopias

CostoEncargo = round(CostoPrimeraCopia_total, 2) + round(CostoRestoCopias, 2)


print("El primer libro tendrá un costo de", str(CostoPrimeraCopia_total)+"$\n")
print("La primera copia costará", str(round(CostoPrimeraCopia, 2)),"y las", CantidadCopias,"copias restantes tienen un costo de", str(round(CostoRestoCopias, 2))+"$\n")


print("El costo total del encargo es de", str(CostoEncargo)+"$")



   
    

    




