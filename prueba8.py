def tablaindividual (numero):
    contador = 0
    while contador <= 10:
        print(f"{numero} x {contador} = {numero * contador}")
        print("")
        contador += 1
    print("\nEso fue todo jejeje")

def tablastodas ():
    num = 1
    while num <= 10:
        print(f"Tabla {num}:")
        contador = 0
        while contador <= 10:
            print(f"{num} x {contador} = {num * contador}")
            print("")
            contador += 1
        print("-------------------------------------")
        num += 1

def programa ():
    print("Bienvenido al programa para mostrar tablas de multiplicar.\n")
    print("Quieres imprimir solo una tabla o todas?\n\t1.Solo una\n\t2.Todas\n")
    option = int(input("Opción: "))

    if option == 1:
        numero = int(input("Que tabla quieres imprimir (De la tabla del 1 a la del 10 nomas)? "))
        if numero < 1 or numero > 10:
            print("Numero no valido. Intente de nuevo")
            programa()
        else:
            tablaindividual(numero)
    elif option == 2:
        tablastodas()
    else:
        print("Opcion no valida. Intente de nuevo")
        programa()

programa()


