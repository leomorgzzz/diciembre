#Calculadora de IMC: Calcula el Índice de Masa Corporal basado en el peso y la altura.

def programa():
    print("Bienvenido al programa para calcular tu IMC")
    nombre = input("Ingresa tu nombre: ")

    print(f"Ahora, {nombre} vas a ingresar tu peso y altura.")
    peso = float(input("Ingresa tu peso en kg: "))
    if peso < 0:
        print("Peso no valido vuelve a intentar.")
        programa()

    altura = float(input("Ingresa tu altura en metros: "))
    if altura < 0:
        print("Altura no valida vuelve a intentar.")
        programa()
    
    resultado = peso/(altura * altura)
    resultado = "{:.2f}".format(resultado)
    print(f"{nombre}, tu IMC es {resultado}")

programa()