#MULTIPLICAR 2 NUMEROS SIN USAR *
n1 = int(input("INGRESE UN NUMERO:"))
n2 = int(input("INGRESE UN NUMERO:"))
x = int(0)
while n2!=0:
	x = x + n1
	n2 = n2 - 1
print(x)