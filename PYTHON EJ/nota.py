#promedio de 3 notas, ver si aprobo o no
n1=int(input("Ingrese el primer numero : "))
n2=int(input("Ingrese el segundo numero : "))
n3=int(input("Ingrese tercer numero : "))
res=((n1+n2+n3)/3)
if res >40:
    print("aprobo")
elif res <40:
    print("reprobo")
input("presione Enter para salir")