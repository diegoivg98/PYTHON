import msvcrt
def main():

#primer argumento cantidad de HORA
#segundo argumento cantidad de MINUTO
#TERCER ARGUMENTO cantidad SEGUNDO

    r=calc(10,13,6)
    s=calc(66,70,80)
    print(r)
    print(s)
    print("Presione una tecla para salir")

def calc(x,y,z):
	if x<=23 and y<=59 and z<=59 and x>=0 and y>=0 and z>=0:
		#CUMPLE CON HORA MINUTO SEGUNDO
		r1="OK"
		return r1

	else:
		#NO VALIDA UNA HORA MINUTO SEGUNDO
		r2="NO"
		return r2

		
 		




if __name__=="__main__":
    main()
    msvcrt.getch()