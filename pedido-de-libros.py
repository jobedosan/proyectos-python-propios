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

Libro_Precio = input("Ingresa el precio del libro a ordenar: \n")

if Libro_Precio.find(",") == -1 and Libro_Precio.find(".") == -1 :
    Libro_Precio = int(Libro_Precio)
else:
    Libro_Precio = float(Libro_Precio)

Libro_Descuento = input("Ingresa el porcentaje de decuento aplicado al libro ordenado: \n")

if Libro_Descuento.find(",") == -1 and Libro_Descuento.find(".") == -1 :
    Libro_Descuento = int(Libro_Descuento)
else:
    Libro_Descuento = float(Libro_Descuento)
    
Libro_con_descuento = Libro_Precio - (Libro_Descuento * Libro_Precio / 100)
Libro_con_descuento = round(Libro_con_descuento, 2)

Precio_envio_primera_copia = input("Ingrese el precio del envío para la primera copia: \n")

if Precio_envio_primera_copia.find(",") == -1 and Precio_envio_primera_copia.find(".") == -1 :
    Precio_envio_primera_copia = int(Precio_envio_primera_copia)
else:
    Precio_envio_primera_copia = float(Precio_envio_primera_copia)

Libro_copia_1 = Libro_con_descuento + Precio_envio_primera_copia
    
cantidad_de_copias = int(input("Ingrese la cantidad de copias a ordenar: \n"))-1

envio_resto_copias = input("Ingrese el precio de envío para las copias restantes: \n")

if envio_resto_copias.find(",") == -1 and envio_resto_copias.find(".") == -1 :
    envio_resto_copias = int(envio_resto_copias)
else:
    envio_resto_copias = float(envio_resto_copias)

precio_resto_copias = (Libro_con_descuento + envio_resto_copias) * cantidad_de_copias

precio_pedido = precio_resto_copias + Libro_copia_1

print(f"El costo del pedido es de {precio_pedido}$, la primera copia con envío incluído cuesta {Libro_copia_1}$ y el costo del resto de copias en su totalidad es de {precio_resto_copias}$")