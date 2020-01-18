def funcion_disc(x):
    """Parameters: int-> int
    OBJ: Comprueba con x el valor de f(x) dependiendo del valor de x"""

    if (x < 1):
        return(x**2-3*x)
    elif (x == 1):
        return(10)
    else:
        return(4*x+2)


print(funcion_disc(2))
