import msvcrt
def main():

#primer argumento un monto en pesos chilenos
#segundo argumento un 1, un 2 o un 3
    r=calc(1,1)
    s=calc(1,2)
    t=calc(1,3)
    print()
    print("Presione una tecla para salir")

def calc(x,y):
	if y==1:
		#CLP A DOLAR
		res1 = (x * 0.0014)
		print("la conversion en dolar es: " +  str(res1))   
		

	elif y==2:
		#CLP A EUROS
		res2 = x*0.0013
		print("la conversion en euros es: " +  str(res2))   

	elif y==3:
		#CLP A YENES
		res3 = x*0.15
		print("la conversion en yenes es: " +  str(res3))   
		




if __name__=="__main__":
    main()
    msvcrt.getch()
