peso = input("INGRESE SU PESO EN KG: ")
estatura = input("INGRESE SU ESTATURA EN METROS: ")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))