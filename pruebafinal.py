print("Bienvenido al programa para convertir un mensaje a un código oculto.\nUsando el cifrado Cesár.")
mensaje = input("Ingrese el mensaje que desea convertir: ").lower()
clave = int(input("Ingrese la clave para el cifrado: "))

resultado = ""
elementos = "abcdefghijklmnñopqrstuvwxyz"
for letra in mensaje:
    if letra.isalpha(): 
        indice_original = elementos.index(letra)
        indice_nuevo = (indice_original + clave) % len(elementos)
        nueva_letra = elementos[indice_nuevo]
        resultado += nueva_letra
    else:
        resultado += letra
print(f"El mensaje cifrado es: {resultado}")  