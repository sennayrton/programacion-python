# Actividad pila parentesis
# Una pila de datos como por ejemplo una pila de platos al ponerlos en un lavavajillas


def esta_vacia(pila):
    """ lista -> bool
    OBJ: Recibe una pila e indica si está vacía o no."""
    if pila:
        return False  # no vacia
    else:
        return True  # Vacia


def introducir(pila, elemento):
    """ lista, char -> lista
    OBJ: Recibe una pila y un elemento y lo introduce en la misma"""
    pila.append(elemento)
    return(pila)


def sacar(pila):
    """ lista -> char
    OBJ: Recibe una pila y devuelve la cima de la pila.
    PRE: La pila no está vacía"""
    return pila.pop()


def comprobar_parentesis(cadena_parentesis):
    """ string -> bool
    OBJ: Recibe una cadena con paréntesis y comprueba que están bien colocados.
    PRE: Sólo hay paréntesis en la cadena y no otros caracteres."""

    mal_colocados = False
    i = 0
    while i < len(cadena_parentesis) and not mal_colocados:
        if cadena_parentesis[i] == "(":
            introducir(pila, "(")
        elif cadena_parentesis[i] == ")":
            if esta_vacia(pila):
                mal_colocados = True
            else:
                elemento = sacar(pila)
        i += 1

    if esta_vacia(pila) and not mal_colocados:
        return True
    else:
        return False


pila = []
cadena_parentesis = input("Introduce una cadena de paréntesis: ")
if comprobar_parentesis(cadena_parentesis):
    print("Paréntesis bien colocados")
else:
    print("Paréntesis mal colocados")
