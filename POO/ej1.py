#Crear una función con tres parámetros que sean números que se suman entre sí.
#Llamar a la función en el main y darle valores.

#Crear una clase coche.
#Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
#Una función que incremente el número de puertas que tiene el coche.
#Crear un objeto miCoche en el main y añadirle una puerta.
#Mostrar el número de puertas que tiene el objeto.

def suma(a,b,c):
    return a + b + c

class coche:
    def __init__(self):
        self.numpuertas = 4
    
    def sumpuertas(self):
        self.numpuertas += 1

if __name__ == '__main__':
    a = 1
    b = 2
    c = 3 
    print("resultado de la suma: "+str(suma(a,b,c)))

    miCoche = coche()
    miCoche.sumpuertas()
    miCoche.sumpuertas()
    print ("numero de puertas: "+str(miCoche.numpuertas))