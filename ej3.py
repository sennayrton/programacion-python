#Ejercicio 3
matriz =  [["avion","tren","coche"] , ["cohete","bicicleta","coche"], ["cohete","bicicleta","coche"]]
 
for i in range(0, 3):
    for j in range(0, 3):
        valor = matriz[i][j]
        if valor == "coche":
            matriz[i][j] = "moto"
        else:
            matriz[i][j] 
 
print (matriz)

