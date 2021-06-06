class Pila:
  def __init__(self):
    self.__crear()
  def __crear(self):
    self.__elementos = []
  def push(self, elem):
    self.__elementos.append(elem)
  def pop(self):
    if not self.isEmpty():
      self.__elementos.pop()
  def top(self):
    return self.__elementos[self.__elementos.__len__()-1]
  def isEmpty(self):
    return self.__elementos == []
        
class Persona:
  def __init__(self, nombre, apellido):
    self.__nombre = nombre
    self.__apellido = apellido
  def getNombre(self):
    return self.__nombre
  def getApellido(self):
    return self.__apellido

p = Pila()
p.push(Persona('Kliber', 'Cerda'))
p.push(Persona('Milovan', 'Charnock'))
p.push(Persona('Erik', 'Garcia'))
p.push(Persona('Cristopher', 'Orellana'))
p2 = Pila()

while(not p.isEmpty()):
   p2.push(p.top())
   p.pop()

while(not p2.isEmpty()):
   persona = p2.top()
   print (persona.getApellido())
   p2.pop()
   
    





