def binarioadecimal():
	nb = '10101'
	pos = len(nb) - 1
	nd = 0
	print ("NUMERO BINARIO:",nb)

	for num in nb:
		digito = int(num)
		mult = digito * 2 ** pos
		print(f'Dígito: {digito}, posición: {pos}, multiplicación: {mult}')
		nd += int(num) * 2 ** pos
		pos -= 1 

	print("NUMERO DECIMAL:",nd)

binarioadecimal()