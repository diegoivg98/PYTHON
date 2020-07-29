import msvcrt
def main():

#reciba un string como argumento
    r=calc("diego")
    print(r)
    print()
    print("Presione una tecla para salir")

def calc(n):
	res= len(n)
	#retorna el largo del string
	return res
	


if __name__=="__main__":
    main()
    msvcrt.getch()