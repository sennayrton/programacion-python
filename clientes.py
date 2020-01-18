clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        dni = input('Introduce DNI del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        fecha = input('Introduce la fecha de nacimiento del cliente: ')
        tipo = input('Introduce el tipo de sus ultimas 5 compras: ')
        media = input('Introduce la cantidad media mensual del gasto: ')
        cliente = {'nombre': nombre, 'dirección': direccion,
                   'fecha': fecha, 'tipo': tipo, 'media': media}
        clientes[dni] = cliente
    if opcion == '2':
        dni = input('Introduce DNI del cliente: ')
        if dni in clientes:
            del clientes[dni]
        else:
            print('No existe el cliente con el dni', dni)
    if opcion == '3':
        dni = input('Introduce DNI del cliente: ')
        if dni in clientes:
            print('DNI:', dni)
            for key, value in clientes[dni].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el dni', dni)
    if opcion == '4':
        print('Lista de clientes')
        for key, value in clientes.items():
            print(key, value['nombre'])
    if opcion == '5':
        print('Ordenados')
        for key, value in clientes.items():
            if value['media']:
                print(key, value['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes ordenados\n(6) Terminar\nElige una opción:')
