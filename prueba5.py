def contarVocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0

    for l in palabra:
        if l in vocales:
            contador += 1
    
    return contador

print("Bienvenido al programa para contar cuantas vocales tiene una palabra\n\n")

palabrausuario = input("Ingresa una palabra: ")
numerovocales = contarVocales(palabrausuario)
print(f"La palabra '{palabrausuario}' tiene {numerovocales} vocales")