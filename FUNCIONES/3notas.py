#calcular promedio de 3 notas
#crear funcion que calcule el promedio, devolver 0 si reprueba, 1 si aprueba o 999 si hay error 
import msvcrt
def main():
	n1=float(input("Ingrese primera nota : "))
	n2=float(input("Ingrese segunda nota : "))
	n3=float(input("Ingrese tercera nota : "))
	r=calc(n1,n2,n3)
	print()
	print(str(r))
	print("Presione una tecla para salir")

def calc(x,y,z):
	#3 notas y promedio
    res = (x+y+z)/3

    if res<4.0 and res>0.0:
    	#REPROBADO
    	return 0
    elif res>=4.0 and res<=7.0:
    	#APROBADO
    	return 1
    else:
    	#ERROR EN EL PROMEDIO
    	return 999

if __name__=="__main__":
    main()
    msvcrt.getch()