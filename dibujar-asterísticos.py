
usuario = input("Introduce el número de filas a crear: ")
for i in range(1, int(usuario) + 1):
    for x in range(i):
        print("*", end = " ")
    print()
