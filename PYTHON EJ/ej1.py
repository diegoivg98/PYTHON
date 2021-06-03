print("Esto es un output con python")
# no hay declaracion de variables solo se utilizan
nom=input("Ingrese su nombre : ")
print("Hola "+nom+" Bienvenido a python")
# Ejemplo de matematicas
n1=int(input("Ingrese el primer numero : "))
n2=int(input("Ingrese el segundo numero : "))
#la funcion float() permite transformar a real
res=n1+n2
print("El resultado es : "+str(res))
#str permite transformar de numerico a string
if res==100:
    print("El resultado es 100")
    print("Esta instruccion esta dentro del if")
print("y esta instruccion no esta condicionada por el if")
# segundo ejemplo if elif
if res >100:
    print("Es mayor que 100")
elif res <100:
    print("ES menor que 100")
elif res <100 and res >10:
    print("Esta entre 101 y 11")
# Ahora con else
if res!=100:
    print("Es distinto de 100")
elif res==1 or res==70:
    print("Es 1 0 70")
elif res==2 or res==70:
    print("Es 2 o 70")
else:
    print("Entonces es cualquier cosa")
#ciclos while
i=1
while i<20:
    print("Es la iteracion : "+str(i))
    i+=1 #i=i+1
op=2
while op!=3:
    print("1 - insultar")
    print("2 - Alabar")
    print("3 - Salir")
    op=int(input("Ingrese su opcion : "))
    if op==1:
        print("usted es un #$#$%$&$&&$$&!!!!")
    elif op==2:
        print("es un buen programador")
    else:
        print("Adios...")
#ciclos for
for x in range(6):
  print(x)
for x in range(2, 6):
  print(x)
for x in range(2, 30, 3):
  print(x)
# recorriendo una lista
seres = ["perro", "gato", "laucha"]
for p in seres:
  print(p)
# recorriendo un string
for b in "una laucha se subio a la mesa":
  print(b)
frutas = ["pera", "platano", "manzana"]
for f in frutas:
  if f == "platano":
    break # interrumpe un ciclo repetitivo
  print(x) # esta fuera del if