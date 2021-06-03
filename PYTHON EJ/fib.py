#serie fibonacci 35 numeros
x=1
y=0
for a in range(0,35):
	z=x+y
	x=y
	y=z
	print (z)