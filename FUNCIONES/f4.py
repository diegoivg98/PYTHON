import msvcrt
def main():

    a = input("Ingrese una palabra: ")
    r=calc(a)
    print(r)
    print("Presione una tecla para salir")

def calc(n):
    #si el largo de la palabra es mayor a 10 y menor que 100
	if len(n)>10 and len(n)<100:
		#CUMPLE CON LAS CONDICIONES
		n="OK"
		return n
	else:
		#NO CUMPLE
		n="NO"
		return n


if __name__=="__main__":
    main()
    msvcrt.getch()
