#promedio de 3 notas, ver si aprobo o no
n1=int(input("Ingrese primera nota: "))
n2=int(input("Ingrese segunda nota: "))
n3=int(input("Ingrese tercera nota: "))
res=((n1+n2+n3)/3)
if res >40:
    print("1(APROBADO)")
elif res <40:
    print("0(REPROBADO)")
input("presione Enter para salir")