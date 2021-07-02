asignaturas = ["Lenguaje","Matematica","Quimica","Fisica"]
aprobada = []
for asignatura in asignaturas:
	nota = float(input("¿Qué nota has sacado en " + asignatura + "?: "))
	if nota >= 4.0:
		aprobada.append(asignatura)

for asignatura in aprobada:
	asignaturas.remove(asignatura)
print("tienes que repetir " + str(asignaturas))
