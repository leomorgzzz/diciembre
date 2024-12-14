def mostrar(lista):
    if not lista:
        print("La lista de compras está empty o sea vacia")
    else:
        print("Lista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    print("")
def agregar(lista):
    item = input("Ingresa el nombre del item que quieres agregar: ")
    lista.append(item)
    print(f"'{item}' ha sido agregado a la lista de compras")
    print("")
def eliminar(lista):
    mostrar(lista)
    if lista:
        try:
            indice = int(input("Ingrsa el numero de articulo que quieres eliminar: ")) - 1
            if 0 <= indice < len(lista):
                itemeliminado = lista.pop(indice)
                print(f"{itemeliminado} ha sido eliminado de la lista")
                print("")
            else:
                print("Numero no valido. No se elimino ningun articulo")
        except ValueError:
            print("Por favor ingresa un numero valido\n")
def menu():
    lista = []
    while True:
        print("----- Menú de Lista de Compras -----")
        print("1. Mostrar lista de compras")
        print("2. Agregar artículo")
        print("3. Eliminar artículo")
        print("4. Salir")
        option = int(input("Selecciona una opción (1-4): "))

        if option == 1:
            mostrar(lista)
        elif option == 2:
            agregar(lista)
        elif option == 3:
            eliminar(lista)
        elif option == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Vuelva a intentar")
            menu()
menu()