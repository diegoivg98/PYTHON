#crear funcion convertir dolares a euros
import msvcrt
def main():

    a = float(input("Ingrese cantidad dolar :"))
    calc(a)
    print()
    print("Presione una tecla para salir")

def calc(n):
    #dolar a euro
    res = (n * 0.9)
    print("La conversion en euros es: " +  str(res))   

if __name__=="__main__":
    main()
    msvcrt.getch()