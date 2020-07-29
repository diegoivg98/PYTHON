import msvcrt
def main():

	a = int(input("Ingrese un numero :"))
	b = int(input("Ingrese otro numero :"))
	r=calc(a,b)
	print(r)
	print("Presione una tecla para salir")

def calc(x,y):
	if x==y:
		#si los dos son iguales
		return 0
	elif x>y:
		#si n1 es mayor que n2
		return 1
	elif y>x:
		#si n2 es mayor que n1 
		return 2
		#error de parametro
	else:
		return 999
	

		
	
		  

if __name__=="__main__":
    main()
    msvcrt.getch()