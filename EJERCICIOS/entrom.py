#CONVERTIR ENTERO A ROMANO 
import sys
lista_dec = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
lista_rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
while True:
	print("")
	num = int(input("INGRESE UN NUMERO DEL 1 AL 1000: "))
	if num==0:
		break
	i=0
	while num>0:
		if num >= lista_dec[i]:
			print(lista_rom[i],end=' ')
			num = num - lista_dec[i]
		else:
			i = i + 1
