#CONVERSOR NUMERO A LETRAS
num = int(input("INGRESE UN NUMERO DEL 0 AL 999: "))
centena = int(num/100)
decena = int((num -(centena * 100))/10)
unidad = int(num - (centena * 100 + decena * 10))

lista_unidad = ["CERO",("UN" , "UNO"),"DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"]
lista_decena = ["",("DIEZ","ONCE","DOCE","TRECE","CATORCE","QUINCE","DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE"),
					("VEINTE","VEINTI"),("TREINTA","TREINTA Y "),("CUARENTA" , "CUARENTA Y "),
					("CINCUENTA" , "CINCUENTA Y "),("SESENTA" , "SESENTA Y "),
					("SETENTA" , "SETENTA Y "),("OCHENTA" , "OCHENTA Y "),
					("NOVENTA" , "NOVENTA Y ")
				]
lista_centena = ["",("CIEN","CIENTO"),"DOSCIENTOS","TRESCIENTOS","CUATROCIENTOS","QUINIENTOS","SEISCIENTOS","SETECIENTOS","OCHOCIENTOS","NOVECIENTOS"]

txt_centena = ""
txt_decena = ""
txt_unidad = ""
txt_centena = lista_centena[centena]
if centena == 1:
	if (decena + unidad)!=0:
		txt_centena = txt_centena[1]
	else:
		txt_centena = txt_centena[0]

txt_decena = lista_decena[decena]
if decena == 1:
	txt_decena = txt_decena[unidad]
elif decena > 1:
	if unidad != 0:
		txt_decena = txt_decena[1]
	else:
		txt_decena = txt_decena[0]

if decena != 1:
	txt_unidad = lista_unidad[unidad]
	if unidad == 1:
		txt_unidad = txt_unidad[0]

print(txt_centena,txt_decena,txt_unidad)