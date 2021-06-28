#CONVERSOR OCTAL A DECIMAL
oc = '14'
pos = len(oc) - 1
nd = 0
print ("NUMERO OCTAL:",oc)

if oc == '9':
	print("NO ES UN OCTAL")
else:
	for num in oc:
		digito = int(num)
		mult = digito * 2 ** pos
		print(f'Dígito: {digito}, posición: {pos}, multiplicación: {mult}')
		nd += int(num) * 8 ** pos
		pos -= 1 

print("NUMERO DECIMAL:",nd)
