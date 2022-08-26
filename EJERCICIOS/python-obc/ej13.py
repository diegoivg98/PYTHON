#Crear clase Vehiculo
class Vehiculo:
    #color, ruedas y puertas como atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    #implementar el método __str__ y retornar un string
    def __str__(self):
        return "Color {}, {} ruedas, {} puertas".format( self.color, self.ruedas, self.puertas )

#Clase Coche hereda de la clase Vehiculo
class Coche(Vehiculo):
    #nuevo atributo para Coche como velocidad y cilindrada
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, {} ruedas, {} puertas, {} km/h, {} cc".format( self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)

coche = Coche('rojo', 4, 4, 120, 1150)
print(coche)