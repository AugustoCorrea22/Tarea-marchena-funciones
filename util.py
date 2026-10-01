def elegir_opcion(lista):
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

    opcion = input("Elegí una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(lista):
        print("Esa opción no es válida, probá de nuevo.")
        opcion = input("Elegí una opción: ")

    return lista[int(opcion) - 1]


frutas = ["Manzana", "Banana", "Naranja", "Pera"]
elegida = elegir_opcion(frutas)
print("Elegiste:", elegida)
