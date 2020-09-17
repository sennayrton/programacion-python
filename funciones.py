def factorial(n):
    """Calcula el factorial"""
    resul = 1
    for i in range(1, n + 1):
        resul *= i
    return resul


print(factorial(5))


def operar(a, b):
    suma = a + b
    resta = a - b
    print(suma, resta)


print(operar(5, 7))


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
