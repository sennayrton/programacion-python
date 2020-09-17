# POO en PYTHON

class Moto():

    # atributos el init es el constructor o inicializador

    def __init__(self, marca):
        self.marca = marca

    # Metodos

    def acelerar(self):
        print("La moto {} esta acelerando".format(self.marca))

    def frenar(self):
        print("La moto {} esta frenando".format(self.marca))


Moto_de_sergio = Moto("BMW")
Moto_de_sergio.acelerar()

Moto_de_alvaro = Moto("Ducati")
Moto_de_alvaro.frenar()

#GETTERS Y SETTERS
#GET->ACCEDER Y SET->MODIFICAR

