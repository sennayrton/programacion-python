# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

dict = {}
cadena = input("Introduzca una cadena:")
for caracter in cadena:
    if caracter in dict:
        dict[caracter] += 1
    else:
        dict[caracter] = 1

for campo, veces in dict.items():
    print(campo, "aparece", veces, "veces")
