print("Bienvenido al programa que suma números.\n\n")

cantidad = int(input("Cuantos números quieres sumar? "))

contador = 1
numt = 0
while contador <= cantidad:
    nums = float(input(f"Ingrese el número {contador}: "))
    contador += 1
    numt += nums


resultado = numt
print(f"La suma de es {resultado}.")