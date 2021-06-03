#ingresar datos como el usuario pueda
#si el largo es mayor a 10 y menor que 100 devolver OK, de no cumplir devolver NO 
import msvcrt
def main():
    a = input("Ingrese una palabra :")
    r=calc(a)
    print(r)
    print("Presione una tecla para salir")

def calc(n):
	if len(n)>10 and len(n)<100:
		#CUMPLE CON LAS CONDICIONES
		n="OK"
		return n
	else:
		#NO CUMPLE LA CONDICION
		n="NO"
		return n

if __name__=="__main__":
    main()
    msvcrt.getch()