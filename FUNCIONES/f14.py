import msvcrt
def main():

	#odio al oso=adia al asa
    r=calc("odio al oso")
    print(r)
    print()

def calc(n):
	#REEMPLAZA LAS O por A 
	res=n.replace("o","a")
	return res	
	


if __name__=="__main__":
    main()
    msvcrt.getch()
