#INGRESAR UN NUMERO Y OBTENER SU TABLA DE MULTIPLICAR DEL 1 AL 10
num = int(input("INGRESA UN NUMERO: "))
res = 0

for x in range(1,11):
	res = num * x
	print(num,"X",x," = ",res)
	x += 1