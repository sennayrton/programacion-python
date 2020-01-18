def sustituye_it(lista_pal, pal_busc, pal_reemp):
    """ lista, string, string -> lista
OBJ: Recibe una lista de palabras, busca todas las apariciones de la palabra a buscar(pal_bus) y la sustituye por la palabra a reemplazar (pal_reemp).
Devuelve la lista de palabras con las sustituciones realizadas."""


pal_reemp = "Coche"
lista_pal = ["Avión", "Tren", "Coche", "Cohete", "Bicicleta", "Coche"]
pal_busc = ""
for p in lista_pal:
    if p == pal_reemp:
        pal_busc += " " + 'Moto'
    else:
        pal_busc += " " + p

print(pal_busc)
