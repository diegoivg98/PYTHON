class SegundaLleyNewton:
    def __init__(self, masa, aceleracion):
        self.__masa = masa
        self.__aceleracion = aceleracion

    def getMasa(self):
        return self.__masa

    def getAceleracion(self):
        return self.__aceleracion

    def getFuerza(self):
        return self.__masa * self.__aceleracion


sln = SegundaLleyNewton(5, 7)
print(sln.getMasa())
print(sln.getAceleracion())
print(sln.getFuerza())
