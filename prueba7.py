import random
def adivinacion ():
    numerosecreto = random.randint(1,10)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de Adivina el Numerin Tilin")
    print("He elegido un numerin tilin entre el 1 y 10. Intenta adivinarlo jejeje")

    while not adivinado:
        try:
            intento = int(input("Ingresa tu intento: "))
            intentos += 1
            if intento < 1 or intento > 10:
                print("Por favor, ingresa numero entre el 1 y 10")
                continue
            if intento < numerosecreto:
                print("Demasiado bajo. Otra vez")
            elif intento > numerosecreto:
                print("Demasiado alto. Otra vez")
            else:
                adivinado = True
                print("Felicidades!!!!!!")
                print(f"Has adivinado el numero {numerosecreto} en {intentos} intentos")
        except ValueError:
            print("Por favor, ingresa un numero valido")
adivinacion()