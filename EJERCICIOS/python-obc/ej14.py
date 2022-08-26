#Crear clase Alumno
class Alumno():
    #nombre y nota como atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return "Alumno:{}, Nota:{}".format(self.nombre, self.nota)
        
    #verificar si el alumno aprueba o reprueba    
    def res(self):
        if self.nota >= 4.0:
            print('APROBADO')
        else:
            print('REPROBADO')

alumno = Alumno('Diego', 7)
alumno.res()
print (alumno)