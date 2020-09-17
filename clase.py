def menor_que_dos(x):
    if x<2:
        print("Menor que 2")
    elif x>=10 and x<=20:
        print("Menor que 20 y mayor que 10")
    elif x>20:
        print("Mayor que 20")
    else: 
        print("Otro valor 2-9")
        n= int(input("Introduce un valor numerico dec 2 a 9: "))
n= int(input("Introduce un valor numerico: "))
print(menor_que_dos(n))