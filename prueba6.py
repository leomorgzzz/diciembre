def menu ():
    print("Deseas convertir de\n\n")
    print("\t1.C° - F°")
    print("\t2.F° - C°\n")

print("Bienvenido para Convertir de de Celsius a Fahrenheit y viceversa")
menu()
option = int(input("Opción: "))

if option == 1:
    celsius=float(input("\n\nIngrese la temperatura en grados Celsius: "))
    operation = (celsius * (9/5)) + 32
    print("\n")
    print(f"{celsius}° grados Celsius es igual a {operation}° grados Fahrenheit")

elif option == 2:
    fah = float(input("\n\nIngrese la temperatura en grados Fahrenheit: "))
    operation = (fah - 32) * (5/9)
    print("\n")
    print(f"{fah}° grados Fahrenheit es igual a {operation}° grados Celsius")

else:
    print("Opción no válida")
