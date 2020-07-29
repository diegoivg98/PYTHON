import msvcrt
def main():

#reciba un string como argumento
    r=calc("diego")
    print(r)
    print()
    print("Presione una tecla para salir")

def calc(n):
	res=n.upper()
	#retorna en mayuscula
	return res
	


if __name__=="__main__":
    main()
    msvcrt.getch()