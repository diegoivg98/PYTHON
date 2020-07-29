import msvcrt
def main():


    a = input("Ingrese un si o no: ")
    r=calc(a)
    print(r)
    print("Presione una tecla para salir")

def calc(n):
	if n=="si" or n=="no":
		#CUMPLE LOS CASOS
		n="CORECTO"
		return n
	else:
		#NO CUMPLE
		n="INCORRECTO"
		return n


if __name__=="__main__":
    main()
    msvcrt.getch()
