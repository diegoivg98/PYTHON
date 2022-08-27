# It imports the pickle module.
from pickle import *

# It creates a class called Vehiculo.
class Vehiculo:
    def __init__(self, marca):
# Creating an attribute called marca.
        self.marca = marca
    
    def __str__(self):
        return('Marca: {}'.format(self.marca))

vehiculo = Vehiculo('Ford')
print(vehiculo)

f = open("vehiculo","w+b")
dump(vehiculo, f)

f.seek(0)
nuevo_vehiculo = load(f)

print(nuevo_vehiculo)
f.close()