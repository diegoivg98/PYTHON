binario = 0
exp = 0
num = int(input("INGRESE UN NUMERO DECIMAL:"))
print("NUMERO DECIMAL:",num)
while num!=0:
	res = num % 2
	binario += (res*pow(10,exp))
	exp = exp+1
	num = int(num/2)

print("NUMERO BINARIO:",binario)