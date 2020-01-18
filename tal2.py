# TAL2.
# 1. Realizar un programa que realice diferentes operaciones sobre listas de registros.

fecha1 = [26, 1, 1856]
fecha2 = [4, 6, 1904]
fecha3 = [7, 6, 1767]
fecha4 = [4, 4, 1967]

autor1 = ["Miguel", "Cervantes", "español", fecha1]
autor2 = ["Valle", "Inclan", "español", fecha2]
autor3 = ["Rosa", "Maria", "mexico", fecha3]
autor4 = ["Garcia", "Marquez", "colombia", fecha4]

idiomas1 = ["español", "ingles", "chino"]
idiomas2 = ["español", "chino"]
idiomas3 = ["mexico"]
idiomas4 = ["colombia"]

libro1 = ["Don Quijote de la Mancha", "084897", autor1, "Planeta", idiomas1]
libro2 = ["Luces de bohemia", "084896", autor2, "Planeta", idiomas2]
libro3 = ["Crimen y castigo", "084898", autor3, "Porrua", idiomas3]
libro4 = ["Cien años de soledad", "084899", autor4, "Debolsillo", idiomas4]
print("___BIENVENIDO A LA BIBLIOTECA UNIVERSIDAD ALCALA___")
# 1A
print("1A")
libros = [libro1, libro2, libro3, libro4]
print("-Libros a disponibilidad del cliente: ", *libros, sep='\n')
# 1B
print("1B")
for libro in libros:
    idiomas = libro[-1]
    autor = libro[2]
    if autor[2] in idiomas and len(idiomas) == 1:
        print("-Autor sin traduccion:", autor[0], autor[1])
# 1C
# 1C.1
print("1C IT")


def numIdiomas(libros):
    maxIdiomas = 0
    for libro in libros:
        idiomas = libro[-1]
        if len(idiomas) > maxIdiomas:
            maxIdiomas = len(idiomas)
    return maxIdiomas


maxIdiomas = numIdiomas(libros)
for libro in libros:
    idiomas = libro[-1]
    autor = libro[2]
    if len(idiomas) == maxIdiomas:
        print("-Autor con mas traducciones: ", autor[0], autor[1])
# 1C.2
print("1C REC")


def numIdiomasRec(libros):
    if len(libros) == 1:
        return len(libros[0][-1])
    else:
        maxNum = numIdiomasRec(libros[1:])
        if maxNum > len(libros[0][-1]):
            return maxNum
        else:
            return len(libros[0][-1])


maxIdiomas = numIdiomasRec(libros)
for libro in libros:
    idiomas = libro[-1]
    autor = libro[2]
    if len(idiomas) == maxIdiomas:
        print("-Autor con mas traducciones: ", autor[0], autor[1])

# 2. Realizar un programa que realice diferentes operaciones sobre un diccionario.
print("2")
libro1 = ["Don Quijote de la Mancha", "084897", "Planeta", idiomas1]
libro2 = ["Luces de bohemia", "084896", "Planeta", idiomas2]
libro3 = ["Crimen y castigo", "084898", "Porrua", idiomas3]
libro4 = ["Cien años de soledad", "084899", "Debolsillo", idiomas4]
# 2A
print("2A")
libros = [libro1, libro2, libro3, libro4]
print("-LIBROS-")
print("-Informacion de los libros: ", *libros, sep='\n')
print()
print()
autores = [autor1, autor2, autor3, autor4]
print("-AUTORES-")
print("-Informacion de los autores: ", *autores, sep='\n')
# 2B
print("2B")
clave = []
valor = []
for libro in libros:
    clave.append(libro[0])
for autor in autores:
    valor.append(autor[0])
diccionario = dict(zip(clave, valor))
for entry in diccionario:
    print("-{nombreLibro} cuyo autor es:  {nombreAutor}".format(
        nombreLibro=entry, nombreAutor=diccionario[entry]))
# 2C
print("2C")
for libro in libros:
    idiomas = libro[3]
    nombreAutor = diccionario[libro[0]]
    if len(idiomas) == 1:
        print("-Autor sin traduccion: ", nombreAutor)
# 2D. OPCIONAL
# 2D.1 ITERATIVO
print("Opcional IT")
maxIdiomas = numIdiomas(libros)  # obtenemos numero maximo idiomas
for libro in libros:
    idiomas = libro[-1]
    nombreAutor = diccionario[libro[0]]
    if len(idiomas) == maxIdiomas:
        print("-Autor con mas traducciones: ", nombreAutor)
# 2D.2 RECURSIVO
print("Opcional REC")
maxIdiomas = numIdiomasRec(libros)  # obtenemos numero maximo idiomas
for libro in libros:
    idiomas = libro[-1]
    nombreAutor = diccionario[libro[0]]
    if len(idiomas) == maxIdiomas:
        print("-Autor con mas traducciones: ", nombreAutor)
