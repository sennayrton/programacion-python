#el lenguaje quickbasic incluye una instruccion DO...LOOP UNTIL para representar iteraciones de tipo "repetir" (se ejecutan 1 o más veces), reescribe en python pero sin emplear la instruccion break- el siguiente codigo:
#INPUT "Introduce un valor para i: "; i$
# DO
#    print i
#    i = i -1
# LOOP UNTIL i < 7

i = int(input("Introduce un valor numérico: "))
print(i)
i = i-1

while i>=7:
    print(i)
    i = i - 1

print("Se acabó")

