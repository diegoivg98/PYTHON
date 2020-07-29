#serie fibonacci 50 numeros
x=1
y=0
z=0
for a in range(0,50):
	z=x+y
	x=y
	y=z
	print (z)