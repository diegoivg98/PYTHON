num = []
for i in range(7):
	num.append(int(input("INGRESE UN NUMERO GANADOR: ")))
num.sort()
print("Los números ganadores son " + str(num))