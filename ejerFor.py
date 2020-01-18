# Codifique un subprograma que determine si un numero es "estupendo", en los numeros estupendos la suma de las cifras de la parte entera es igual a la suma de las 3 primeras cifras de su parte decimal. por ejemplo, el numero 33.321 es estupendso, y tambien lo son 212.05, 20.101, 63.0 y 45.423


def suma_cifras(x):
    """int -> int
    OBJ: Suma las cifras del numero pasado como argumento"""

    suma = 0

    while x != 0:
        digito = x % 10
        suma = suma + digito
        x = x // 10

    return suma


def es_estupendo(num):
    """float -> bool
    OBJ: Nos indica si la suma de las cifras de la parte entera de "num" es igual a la suma de las 3 primeras cifras de su parte decimal"""

    parte_entera = int(num)
    parte_decimal = 1000*(num - parte_entera)
    return suma_cifras(parte_entera) == suma_cifras(parte_decimal)


if es_estupendo(127.811):
    print("Es estupendo")
else:
    print("No es estupendo")
