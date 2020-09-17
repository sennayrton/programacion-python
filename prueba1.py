#1. Si dos valores enteros dados son iguales o si su suma o diferencia es 5
def enteros_iguales(a,b):
    """Parameters: int, int ->boolean
    OBJ: Comprueba si a es igual a b o si..."""
    import math
    return (a==b) or (a+b==5) or (abs(a-b)==5)

if enteros_iguales(8,8):
    print("Son iguales o...")
else: print("Son diferentes o no suman...")