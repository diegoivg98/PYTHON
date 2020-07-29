import msvcrt
def main():

    a = float(input("Ingrese cantidad grados celsius :"))
    calc(a,1)
    calc(a,2)
    r=calc(a,1)
    r2=calc(a,2)
    print(str(r))
    print(str(r2))
    print("Presione una tecla para salir")

def calc(x,y):
	if y==1:
		#grados FARENHEIT
		res = (x * 9/5)+32
		return res

	elif y==2:
		#GRADOS KELVIN
		res = x+273.15
		return res




if __name__=="__main__":
    main()
    msvcrt.getch()
