exp = 0
decimal = 0
num = int(input("INGRESE UN NUMERO:"))

while (num!=0):
	res = num%10
	decimal += (res*pow(8,exp))
	exp = exp+1
	num = int(num/10)

print("NUMERO DECIMAL:",decimal)