import msvcrt
def main():

#reciba como argumento el lado de un cuadrado
    calc(3)
    print()
    print("Presione una tecla para salir")

def calc(n):
    #muestre su área y su perímetro
    area = (n*n)
    perimetro = (n*4)
    print("El area del cuadrado es: " +  str(area))   
    print("El perimetro del cuadrado es: " +  str(perimetro))   


if __name__=="__main__":
    main()
    msvcrt.getch()
