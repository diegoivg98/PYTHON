def factorial(n):
	cont = 1
	for i in range(n):
		cont *= i+1
	return cont

print(factorial(4))