#JUEGO PIEDRA PAPEL O TIJERA
#MAQUINA VS USUARIO
#MOSTRAR PUNTUACION
import random
from random import choice
print ("Vamos a jugar a Piedra, Papel o Tijera.")

def mi_partida():
    puntuaciones = 0
    Opciones = ['Piedra', 'Papel', 'Tijera'] 
    Maquina = (choice((Opciones)))
    Eleccion = input("Seleccione Piedra, Papel o Tijera: ")
    
    #SI USUARIO INGRESA OTRO DATO
    if Eleccion not in Opciones:
        print ("Seleccione una opción válida")
     
    #CASO EMPATE
    if Eleccion == Maquina:
        puntuaciones = 0
        print("USUARIO saco " + Eleccion)
        print("MAQUINA saco " + Maquina)
        print("Empate")
##################################################################
    #USUARIO SACA PIEDRA, MAQUINA SACA PAPEL
    if (Eleccion == 'Piedra'):
        if (Maquina == 'Papel'):
            puntuaciones = 2
            print("USUARIO saco " + Eleccion)
            print("MAQUINA saco " + Maquina)
            print("Perdiste")
        #USUARIO SACA PIEDRA, MAQUINA SACA PAPEL    
        elif (Maquina == 'Tijera'):
            puntuaciones = 1
            print("USUARIO saco " + Eleccion)
            print("MAQUINA saco " + Maquina)
            print("ganaste")
###################################################################
    #USUARIO SACA PAPEL, MAQUINA SACA TIJERA
    if (Eleccion == 'Papel'):
        if (Maquina == 'Tijera'):
            puntuaciones = 2
            print("USUARIO saco " + Eleccion)
            print("MAQUINA saco " + Maquina)
            print("Perdiste")
        #USUARIO SACA PAPEL, MAQUINA SACA PIEDRA    
        elif (Maquina == 'Piedra'):
            puntuaciones = 1
            print("USUARIO saco " + Eleccion)
            print("MAQUINA saco " + Maquina)
            print("Ganaste")
###################################################################
    #USUARIO SACA TIJERA, MAQUINA SACA PIEDRA
    if (Eleccion == 'Tijera'):
        if (Maquina == 'Piedra'):
            puntuaciones = 2
            print("USUARIO saco " + Eleccion)
            print("MAQUINA saco " + Maquina)
            print("perdiste")
        #USUARIO SACA TIJERA, MAQUINA SACA PAPEL
        elif (Maquina == 'Papel'):
            puntuaciones = 1 
            print("USUARIO saco " + Eleccion)
            print("MAQUINA saco " + Maquina)
            print("ganaste")

    return puntuaciones

def main():
    pJug = 0
    pMaq = 0
    n = False

    while n==False:
        puntuaciones = mi_partida()
        if puntuaciones == 1:
            pJug += 1
        elif puntuaciones == 2:
            pMaq += 1
        print ("Puntuaciones: Maquina ->",pMaq,"||","USUARIO ->",pJug)
        respuesta=input("¿Quieres seguir jugando?: y/n: ")
        if(respuesta == "n"):
            print("Juego finalizado")
            n = True

main()