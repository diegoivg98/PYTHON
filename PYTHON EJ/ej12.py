print("1-ingresar numero")
print("2-salir")
print()
res1=0
res2=0
res3=0
cont=0
cont2=0
cont3=0
res4=0
while True:
    op=int(input("Ingrese su opcion : "))
    if op==1:
        a=int(input("ingrese un numero: "))
        res1=res1+op 
        res2=res2+a 
        res3=res2/res1 
        if a%2==0:
            cont3+=1
        else:
            res4+=1
        if a==7:
            cont+=1
        elif a==21:
            cont2+=1

    elif op==2:
            print()
            print("la cantidad de numeros ingresados es: "+str(res1))
            print("la sumatoria de los numeros es: "+str(res2))
            print("el promedio de los numeros es: "+str(res3))
            print("la cantidad de 7 es: "+str(cont))
            print("la cantidad de 21 es: "+str(cont2))
            print("total pares ingresados: "+str(cont3))
            print("total impares ingresados: "+str(res4))
            print()
            input("presione enter para salir")
            break