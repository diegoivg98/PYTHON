#RECREAR JUEGO PIEDRA PAPEL TIJERA
#CREAR CLASE JUGADOR
#MAQUINA VS MAQUINA
import random
elec=['piedra','papel','tijera']
#CREACION CLASE JUGADOR
class jugador:
    def _init_(self):
        self.el1=0
        self.el2=1
        self.el3=2

    def num_aleat(self):
        return random.randint(0,2)

    def num_aleat2(self):
        return random.randint(0,2)
######################################

jugador1=jugador()
jugador2=jugador()

while True:
    #J1 Y J2 SACAN PIEDRA
    if(jugador1.num_aleat()==0 and jugador2.num_aleat2()==0 ):
        print("J1 elgió : " + elec[0])
        print("J2 elgió : " + elec[0])
        print("ES UN EMPATE")
        break
    
    #J1 Y J2 SACAN PAPEL
    elif(jugador1.num_aleat()==1 and jugador2.num_aleat2()==1 ):
        print("J1 elgió : " + elec[1])
        print("J2 elgió : " + elec[1])
        print("ES UN EMPATE")
        break

    #J1 Y J2 SACAN TIJERA
    elif(jugador1.num_aleat()==2 and jugador2.num_aleat2()==2 ):
        print("J1 elgió : " + elec[2])
        print("J2 elgió : " + elec[2])
        print("ES UN EMPATE")
        break
###################################################################
    #J1 SACA PIEDRA Y J2 SACA PAPEL
    elif(jugador1.num_aleat() == 0 and jugador2.num_aleat2() == 1):
        print("J1 elgió : " + elec[0])
        print("J2 elgió : " + elec[1])
        print("GANA J2")
        break     
    
    #J1 SACA PAPEL Y J2 SACA PIEDRA
    elif(jugador1.num_aleat() == 1 and jugador2.num_aleat2() == 0):
        print("J1 elgió : " + elec[1])
        print("J2 elgió : " + elec[0])
        print("GANA J1")
        break     
###################################################################
    #J1 SACA PIEDRA Y J2 SACA TIJERA
    elif(jugador1.num_aleat() == 0 and jugador2.num_aleat2() == 2):
        print("J1 elgió : " + elec[0])
        print("J2 elgió : " + elec[2])
        print("GANA J1")
        break     
    
    #J1 SACA TIJERA Y J2 SACA PIEDRA
    elif(jugador1.num_aleat() == 2 and jugador2.num_aleat2() == 0):
        print("J1 elgió : " + elec[2])
        print("J2 elgió : " + elec[0])
        print("GANA J2")
        break 
##################################################################
    #J1 SACA PAPEL Y J2 SACA TIJERA
    elif(jugador1.num_aleat() == 1 and jugador2.num_aleat2() == 2):
        print("J1 elgió : " + elec[1])
        print("J2 elgió : " + elec[2])
        print("GANA J2")
        break     

    #J1 SACA TIJERA Y J2 SACA PAPEL
    elif(jugador1.num_aleat() == 2 and jugador2.num_aleat2() == 1):
        print("J1 elgió : " + elec[2])
        print("J2 elgió : " + elec[1])
        print("GANA J1")
        break             
##################################################################