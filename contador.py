acumulador = 0
for var in range (1,10):
    numero = int(input("ingrese numero"))
    if numero % 2==0:
        acumulador = acumulador+numero
print("La suma de los numeros pares es",acumulador)