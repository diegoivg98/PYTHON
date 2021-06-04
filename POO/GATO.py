print (" 0 | 1 | 2 ")
print("-----------")
print (" 3 | 4 | 5 ")
print("-----------")
print (" 6 | 7 | 8 ")

print()
print()

class Tabla(object):
    def __init__(self):
        self.celda = [" "," "," ", " ", " ", " ", " ", " ", " "] ## 9 CELDAS PARA CONTENER X o O

    def update(self, ncelda, jugador):
    	if self.celda[ncelda] == " ":
    		self.celda[ncelda] = jugador

    def ganador(self, jugador):

    	#CASO HORIZAONTAL
    	if self.celda[0]==jugador and self.celda[1]==jugador and self.celda[2]==jugador:
    		return True

    	if self.celda[3]==jugador and self.celda[4]==jugador and self.celda[5]==jugador:
    		return True	

    	if self.celda[6]==jugador and self.celda[7]==jugador and self.celda[8]==jugador:
    		return True	
    #####################################################################################		
    	#CASO VERTICALES
    	if self.celda[0]==jugador and self.celda[3]==jugador and self.celda[6]==jugador:
    		return True	

    	if self.celda[1]==jugador and self.celda[4]==jugador and self.celda[7]==jugador:
    		return True	

    	if self.celda[2]==jugador and self.celda[5]==jugador and self.celda[8]==jugador:
    		return True	
#############################################################################################
    	#CASO DIAGONALES
    	if self.celda[0]==jugador and self.celda[4]==jugador and self.celda[8]==jugador:
    		return True

    	if self.celda[2]==jugador and self.celda[4]==jugador and self.celda[6]==jugador:
    		return True	
    					

    ##MOSTRAR EL DIBUJO DEL JUEGO
    def mostrar(self):
        print(self.celda[0] + ' | ' + self.celda[1] + ' | ' + self.celda[2])
        print('---------')
        print(self.celda[3] + ' | ' + self.celda[4] + ' | ' + self.celda[5])
        print('---------')
        print(self.celda[6] + ' | ' + self.celda[7] + ' | ' + self.celda[8])      
tabla = Tabla()

def main():
    print("ESTE ES EL JUEGO DEL GATO")
main()    
tabla.mostrar()
print()

while True:
	selX = int(input("JUGADOR 1 (X) ESCOGA UN NUMERO DEL 0 AL 8: "))
	print()
	if (selX<0 and selX>=9): #condicion para seleccion del 0 al 8
			print("solo puede ingresar del 0 al 8")
	
	else:
		print()
		tabla.update(selX, "X")#HACE INGRESO "X" A LA CELDA (NUMERO) SELECCIONADO
		tabla.mostrar()
		print()

		if tabla.ganador("X"):
			print ("GANADOR: JUGADOR 1")
			break

		selO = int(input("JUGADOR 2 (O) ESCOGA UN NUMERO DEL 0 AL 8: "))
		print()
		if (selO<0 and selO>=9):#condicion para seleccion del 0 al 8
			print ("solo puede ingresar del 0 al 8")
			
		else:
			print()
			tabla.update(selO, "O") #HACE INGRESO "O" A LA CELDA (NUMERO) SELECCIONADO
			tabla.mostrar()
			print()
			if tabla.ganador("O"):
				print ("GANADOR: JUGADOR 2")
				break