#ingresar 2 numeros y escoger una de las sgtes opciones

print("1 - sumar")
print("2 - restar")
print("3 - multiplicar")
print("4 - dividir")
print("5 - salir")
print()
while True:
    op=int(input("Ingrese su opcion : "))
    if op==1:
        x=int(input("ingrese primer numero: "))
        y=int(input("ingrese segundo numero: "))
        r1=x+y
        print("la suma es: "+str(r1))
    elif op==2:
        x=int(input("ingrese primer numero: "))
        y=int(input("ingrese segundo numero: "))
        r2=x-y
        print("la resta es: "+str(r2))
    elif op==3:
        x=int(input("ingrese primer numero: "))
        y=int(input("ingrese segundo numero: "))
        r3=x*y
        print("el producto es: "+str(r3))
    elif op==4:
        x=int(input("ingrese primer numero: "))
        y=int(input("ingrese segundo numero: "))
        r4=x/y
        print("la division es: "+str(r4))
    elif op==5:
        break