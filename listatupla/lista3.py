asignatura = ["Lenguaje","Matematica","Quimica","Fisica"]
nota = []
for asignatura in asignatura:
	nota = float(input("QUE NOTA SACASTE EN ",asignatura," ?"))
	nota.append(nota)
for i in range(len(asignatura)):
	print("En " + asignatura[i] + " has sacado " + nota[i]))