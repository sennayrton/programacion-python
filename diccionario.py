diccionario = {"one" : 1, "two" : 2, "three" : 3}

print(type(diccionario))

print(diccionario["two"])
dict1={}
dict1["nombre"]="sergio"
dict1["edad"]=21
print(dict1)
print(len(dict1))

print(diccionario.get("one"))

for clave in diccionario.keys():
    print(clave)

for clave, valor in diccionario.items():
    print(clave," ", valor)

