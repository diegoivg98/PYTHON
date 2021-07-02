def area_circulo(radio):
	pi = 3.1415
	return pi*radio**2

def volumen_cilindro(radio,alto):
	return area_circulo(radio)*alto

print(volumen_cilindro(3,5))