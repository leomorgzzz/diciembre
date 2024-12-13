def verificador (result):
    if result == 0:
        print("\nEl número es par")
    else:
        print("\nEl número es impar")

print("Hola, bienvenid@ al programa para saber si un número es par o impar :)\n\n")

numero = int(input("Ingrese el número a checar: "))
result = (numero % 2)
verificador(result)