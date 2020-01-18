class Cliente:
    def __init__(self, nom, direccion, fecha, media, tip):
        self.nombre = nom
        self.direccion = direccion
        self.fecha = fecha
        self.compras = media
        self.tipos = tip


def es_menor(cliente1, cliente2):
    compras_cliente1 = 0
    compras_cliente2 = 0
    for i in range(len(cliente1.compras)):
        compras_cliente1 += cliente1.compras[i]
        compras_cliente2 += cliente2.compras[i]
    return (compras_cliente1 < compras_cliente2)


def ascender(v, inicio, fin):
    for i in range(fin, inicio, -1):
        if es_menor(v[i], v[i-1]):
            temp = v[i]
            v[i] = v[i-1]
            v[i-1] = temp


def burbuja(v, inicio, fin):
    for pasada in range(inicio, fin):
        ascender(v, pasada, fin)


def ordenar(lista):
    """ list, float -> list
        OBJ: Ordena la lista de empleados por ventas
    """
    burbuja(lista_compras, 0, len(lista)-1)
    return lista


def contar_veces(self, elemento, tip):
    veces = 0
    for j in tip:
        if elemento == j:
            veces += 1
    return veces
    print(contar_veces(self, 1, tip))


def mostrar(lista):
    """ list -> None
        OBJ: Muestra la lista de empleados en pantalla
    """
    print('Apartado e: Lista de empleados ordenados de menor a mayor considerando el gasto medio mensual realizado: ')
    for i in lista:
        print(i.nombre)  # Apartado E


def contarElementosLista(tipos):
    """
    Recibe una lista, y devuelve un diccionario con todas las repeticiones de
    cada valor
    """
    return {z: tipos.count(z) for z in tipos}
    # Apartado c, cuenta los tipos repetidos en las listas tipos
    print(contarElementosLista(tipos))

    pregunta = input(
        'Escriba actualizar si desea modificar la información sobre el tipo de sus compras y el importe medio mensual de gasto: ')
    if pregunta == "actualizar":
        clienteActualizarOld = input("Digite el tipo que desea actualizar: ")
        clienteActualizarNew = input("Digite el nuevo tipo: ")
        Cliente[cliente.index(clienteActualizarOld)
                ] = clienteActualizarNew  # Apartado B


lista_compras = []
cliente = Cliente('Angel', 'Calle Petunias', '28-03-1959',
                  [750], ['alimentación y bebidas', 'bebé', 'bebé', 'bebé', 'bebé'])
lista_compras.append(cliente)  # Apartado A
cliente = Cliente('Maria', 'Calle Arboles', '28-04-1959', [350], [
                  'alimentación y bebidas', 'alimentación y bebidas', 'bebé', 'bebé', 'alimentación y bebidas'])
lista_compras.append(cliente)
cliente = Cliente('Carlos', 'Calle Madrid', '02-03-1952', [850], [
                  'belleza', 'deportes y aire libre', 'informática', 'ropa y accesorios', 'bebé'])
lista_compras.append(cliente)
ordenar(lista_compras)
mostrar(lista_compras)
