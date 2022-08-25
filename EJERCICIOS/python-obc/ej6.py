peso = int(input('Ingrese su peso en Kg: '))
estatura = float(input('Estatura en metros: '))
imc = round(float(peso)/float(estatura * estatura),2)

print(peso)
print(estatura)
print("Su indice de masa corporal es: "+ str(imc))