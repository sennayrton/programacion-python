# Crea una aplicación que pida un número y calcule su factorial (El factorial de 
# un número es el producto de todos los enteros entre 1 y el propio número y se 
# representa por el número seguido de un signo de exclamación. 
# Por ejemplo 5! = 1x2x3x4x5=120)

resul = 1
num=int(input("Numero a introducir: "))
contador = 2
while contador <= num:
	resul = resul * contador
	contador = contador + 1
print("El resultado es: ", resul)























