def menu():
    print("¿Qué operación desea hacer?\n\t")
    print("\t1.Suma\n")
    print("\t2.Resta\n")
    print("\t3.Multiplicación\n")
    print("\t4.División")


print("Bienvenido al programa que hace pocas operaciones con números.\n\n")
menu()
option = int(input("Opción: "))

if option == 1:
    cantidad = int(input("¿Cuántos números quieres sumar? "))

    contador = 1
    numt = 0
    while contador <= cantidad:
        nums = float(input(f"Ingrese el número {contador}: "))
        contador += 1
        numt += nums

    resultado = numt
    print(f"La suma es {resultado}.")

elif option == 2:
    cantidad = int(input("¿Cuántos números quieres restar? "))

    contador = 1
    numt = 0
    while contador <= cantidad:
        nums = float(input(f"Ingrese el número {contador}: "))
        contador += 1
        numt -= nums  

    resultado = numt
    print(f"La resta es {resultado}.")

elif option == 3:
    cantidad = int(input("¿Cuántos números quieres multiplicar? "))

    contador = 1
    numt = 1  
    while contador <= cantidad:
        nums = float(input(f"Ingrese el número {contador}: "))
        contador += 1
        numt *= nums  

    resultado = numt
    print(f"La multiplicación es {resultado}.")

elif option == 4:
    print("En división solo usaremos dos valores\n\n")
    num1 = float(input("Ingrese el primer número (Numerador): "))
    num2 = float(input("Ingrese el segundo número (Denominador): "))

    
    resultado = num1/num2
    print(f"La division es {resultado}.")
else:
    print("Opción no válida.")
