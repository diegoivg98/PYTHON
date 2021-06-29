cont=0
decimal=0
num = int(input("INGRESE UN NUMERO BINARIO:"))
print("NUMERO BINARIO:",num)

while (num!=0):
	ult_dig = num % 10
	decimal += (ult_dig * pow(2,cont))
	cont = cont + 1
	num = int(num/10)

print("NUMERO DECIMAL:",decimal)