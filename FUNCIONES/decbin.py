def decimalabinario():
	nd = 5
	lista = [] 
	print("NUMERO DECIMAL:",nd)
	while nd != 0:
		lb = nd % 2
		cociente = nd // 2
		lista.append(lb) 
		nd = cociente 

	print("NUMERO BINARIO:",lista)

decimalabinario()