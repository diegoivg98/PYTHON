#celsius a FARENHEIT o KELVIN
#crear funcion donde el primer dato son los grados celsius y el segundo la opcion 1 o 2
import msvcrt
def main():
    a = float(input("Ingrese cantidad grados celsius :"))

    calc(a,1)
    calc(a,2)

    r1=calc(a,1)
    r2=calc(a,2)
    print(str(r1))
    print(str(r2))
    print("Presione una tecla para salir")

def calc(x,y):
	if y == 1:
		#FARENHEIT
		res = (x * 9/5)+32
		return res

	elif y == 2:
		#KELVIN
		res = x+273.15
		return res

if __name__=="__main__":
    main()
    msvcrt.getch()