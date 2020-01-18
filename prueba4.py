# Realice un subprograma que determine si un numero esta dentro de sus limites naturales, los cuales se pasan como argumento al subprograma.


def numero_limite(num, lim_inf, lim_sup):
    """Parameters: int, int, int -> boolean
    OBJ: Comprueba si un num esta comprendido entre dos limites
    PRE: lim_inf sera menor que lim_sup"""

    return (num >= lim_inf) and (num <= lim_sup)


if (numero_limite(0, 15, 50)):
    print("Dentro limites")
else:
    print("Fuera limites")
