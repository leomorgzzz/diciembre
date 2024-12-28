import re

print("Programa que detecta palabras únicas en una frase.")
frase = input("Ingrese una frase: ")
a = 0
# Dividir la frase en palabras usando múltiples separadores
separadores = r"[ ,.!?]+"
palabras = re.split(separadores, frase)
palabras = [p for p in palabras if p]  # Eliminar cadenas vacías

# Contar la frecuencia de cada palabra
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# Mostrar la frecuencia de palabras
print("\nFrecuencia de palabras:")
for palabra, conteo in frecuencia.items():
    print(f"{palabra}: {conteo}")

print("\nPalabras únicas:")
a = 0  # Inicializamos el contador
for palabra, conteo in frecuencia.items():
    if conteo == 1:
        print(palabra)
        a += 1  # Incrementamos el contador

# Mostrar la cantidad de palabras únicas
print(f"\nNúmero de palabras únicas: {a}")
