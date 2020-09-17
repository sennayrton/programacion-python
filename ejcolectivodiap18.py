def salario_bruto(num_horas, precio_hora):
    """int, float -> float
    OBJ: Calcula el salario bruto"""
    
    if num_horas>40:
        salario=(num_horas-40)*(precio_hora*1.5)+40*precio_hora
    else:
        salario=num_horas*precio_hora

    return(salario)

num_horas = int(input("Introduce el numero de horas: "))
precio_hora = int(input("Introduce el precio por hora: "))
print("El sueldo a pecibir es: ", salario_bruto(num_horas, precio_hora)," euros")


