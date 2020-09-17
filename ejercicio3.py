# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar 
# los precios de las distintas frutas. El programa pedirá el nombre de la fruta 
# y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir 
# de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}

while True:
    fruta = input("¿Que fruta ha sido vendida?:")
    if fruta.lower() not in precios:
        print("Fruta no existe")
    else:
        cantidad = int(input("Cantidad de fruta vendida:"))
        total=(cantidad * precios[fruta])
        print("El precio es: ", total)
    opcion = input("¿Quieres vender otra fruta (si/no)")
    while opcion.lower() != "si" and opcion.lower() != "no":
        opcion = input("¿Quieres vender otra fruta (si/no)")
    if opcion.lower() == "no":
        break



    
