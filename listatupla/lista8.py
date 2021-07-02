palabra = input("ingresa una palabra: ")
palabra_reversa = palabra
palabra = list(palabra)
palabra_reversa = list(palabra_reversa)
palabra_reversa.reverse()
if palabra == palabra_reversa:
	print("es un palindromo")
else:
	print("no es un palindromo")