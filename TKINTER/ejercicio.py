from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import psycopg2

##CONEXION A BASE DE DATOS
try:
	conn = psycopg2.connect("dbname='personal' host='localhost' user='diegoivg98' password='morelloratm2798'")
except:
	print("Hay problemas con la base de datos")
	exit()

class form():
	def __init__(self):
		self.ventana=Tk()
		self.ventana.title("FORMULARIO PERSONAL")
		self.ventana.geometry("580x400+200+100")

		self.ln1=Label(self.ventana,text="RUT: ",font=("Arial",12)).place(x=1,y=10)
		self.rut=StringVar()
		self.en1=Entry(self.ventana,textvariable=self.rut,takefocus=1)
		self.en1.place(x=125,y=15)
		self.en1.focus()	

		self.ln2=Label(self.ventana,text="NOMBRE: ",font=("Arial",12)).place(x=1,y=50)
		self.nombres=StringVar()
		self.en2=Entry(self.ventana,textvariable=self.nombres,takefocus=1)
		self.en2.place(x=125,y=55)
		self.en2.focus()	

		self.ln3=Label(self.ventana,text="APELLIDO: ",font=("Arial",12)).place(x=1,y=90)
		self.apellidos=StringVar()
		self.en3=Entry(self.ventana,textvariable=self.apellidos,takefocus=1)
		self.en3.place(x=125,y=95)
		self.en3.focus()	

		self.ln4=Label(self.ventana,text="EDAD: ",font=("Arial",12)).place(x=1,y=130)
		self.edad=IntVar()
		self.en4=Entry(self.ventana,textvariable=self.edad,takefocus=1)
		self.en4.place(x=125,y=135)
		self.en4.focus()	

		self.btn1=Button(self.ventana,text="LIMPIAR",width=10,command=self.limpiar).place(x=30,y=300)

		self.btn2=Button(self.ventana,text="AGREGAR",width=10,command=self.agregar).place(x=150,y=300)
		self.btn3=Button(self.ventana,text="MODIFICAR",width=10,command=self.modificar).place(x=270,y=300)

		self.btn4=Button(self.ventana,text="ELIMINAR",width=10,command=self.eliminar).place(x=390,y=300)

		self.btn5=Button(self.ventana,text="CAMBIO",width=10,command=self.cambio).place(x=490,y=300)
		self.btn6=Button(self.ventana,text="BUSCAR",width=10,command=self.buscar).place(x=590,y=300)

		self.ventana.mainloop()

	def limpiar(self):	
		self.rut.set("")
		self.nombres.set("")
		self.apellidos.set("")
		self.edad.set("")
		messagebox.showinfo("MESSAGE",message="Se han limpiado los Campos")	

	def agregar(self):
		rut= self.rut.get()
		nombres= self.nombres.get()
		apellidos=self.apellidos.get()
		edad=self.edad.get()
		
		if edad <1 :
			messagebox.showinfo("MESSAGE",message="Ingrese una edad mayor a 0")	

		if (rut=="" or nombres=="" or apellidos=="" or edad<1) :
			messagebox.showinfo("MESSAGE",message="Rellene los campos")	
		else:
			try:
				cur = conn.cursor()
				cur.execute("INSERT INTO personal (rut,nombres,apellidos,edad) VALUES ('"+(rut)+"','"+(nombres)+"','"+(apellidos)+"','"+str(edad)+"')")
				conn.commit()
				cur.close()
				self.en1.focus()
				messagebox.showinfo("MESSAGE",message="DATOS INGRESADOS")	
				self.rut.set("")
				self.nombres.set("")
				self.apellidos.set("")
				self.edad.set("")
			except:
				messagebox.showinfo("MESSAGE",message="ERROR AL INGRESAR")	

	def buscar(self):	

		rut= self.rut.get()
		nombres= self.nombres.get()
		apellidos=self.apellidos.get()
		edad=self.edad.get()

		cur = conn.cursor()
		##Consulta para buscar datos
		cur.execute("SELECT nombres, apellidos, edad FROM personal WHERE rut='"+(rut)+"'")
		##trae todos los datos 
		records = cur.fetchall()
		##SE CARGAN LOS DATOS EN LOS TEXTBOX
		for row in records:
			self.nombres.set(row[0])
			self.apellidos.set(row[1])
			self.edad.set(row[2])
			conn.commit()
			cur.close()

	def modificar(self):	

		rut= self.rut.get()
		nombres= self.nombres.get()
		apellidos=self.apellidos.get()
		edad=self.edad.get()

		try:
			cur = conn.cursor()
			cur.execute("UPDATE personal SET nombres='"+nombres+"',apellidos = '"+apellidos+"',edad = '"+str(edad)+"' WHERE rut='"+(rut)+"'")
			conn.commit()
			cur.close()
			self.en1.focus()
			messagebox.showinfo("MESSAGE",message="DATOS MODICADOS")	
			self.rut.set("")
			self.nombres.set("")
			self.apellidos.set("")
			self.edad.set("")
		except:
			messagebox.showinfo("MESSAGE",message="ERROR AL MODIFICAR")	

	def eliminar(self):	

		rut= self.rut.get()

		try:
			cur = conn.cursor()
			cur.execute("DELETE FROM personal WHERE rut='"+(rut)+"'")
			conn.commit()
			cur.close()
			self.en1.focus()

			messagebox.showinfo("MESSAGE",message="DATOS ELIMINADOS")	
			self.rut.set("")
			self.nombres.set("")
			self.apellidos.set("")
			self.edad.set("")
		except:	
			messagebox.showinfo("MESSAGE",message="ERROR AL ELIMINAR")	

	def cambio(self):
		self.ventana.destroy()
		form2()
###########################SEGUNDO FORMULARIO###############################################################
try:
	con = psycopg2.connect("dbname='vehiculos' host='localhost' user='diegoivg98' password='morelloratm2798'")
except:
	print("Hay problemas con la base de datos")
	exit()

class form2():

	def __init__(self):
		self.ventana2=Tk()
		self.ventana2.title("FORMULARIO VEHICULOS")
		self.ventana2.geometry("580x400+200+100")

		self.ln1=Label(self.ventana2,text="PATENTE: ",font=("Arial",12)).place(x=1,y=10)
		self.patente=StringVar()
		self.en1=Entry(self.ventana2,textvariable=self.patente,takefocus=1)
		self.en1.place(x=125,y=15)
		self.en1.focus()	

		self.ln2=Label(self.ventana2,text="MARCA: ",font=("Arial",12)).place(x=1,y=50)
		self.marca=StringVar()
		self.combo2 = Combobox(self.ventana2,state='readonly',width=8)
		self.combo2['values']= ("Scania", "Man", "Volvo", "Mercedes", "Isuzu", "Hummer", "GMC", "Hino", "Ford", "Mack")
		self.combo2.place(x=125,y=55)
		self.combo2.current(0)	

		self.ln5=Label(text="AÑO : ",font=("Arial",12)).place(x=1,y=90)
		self.año=StringVar()
		self.combo = Combobox(self.ventana2,state='readonly',width=4)
		self.combo['values']= (1960, 1961, 1962, 1963, 1964, 1965, 1965, 1966, 1967, 1968, 1969, 1970,
	1971, 1972, 1973, 1974, 1975, 1976,1977, 1978, 1979, 1980,
	1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 
	1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 
	2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
	2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019)
		self.combo.place(x=125,y=90)
		self.combo.current(0) 


		self.ln4=Label(self.ventana2,text="CARGA: ",font=("Arial",12)).place(x=1,y=130)
		self.carga=StringVar()
		self.en4=Entry(self.ventana2,textvariable=self.carga,takefocus=1)
		self.en4.place(x=125,y=135)
		self.en4.focus()	

		self.btn1=Button(self.ventana2,text="LIMPIAR",width=10,command=self.limpiar).place(x=30,y=300)
		self.btn2=Button(self.ventana2,text="AGREGAR",width=10,command=self.agregar).place(x=150,y=300)
		self.btn3=Button(self.ventana2,text="MODIFICAR",width=10,command=self.modificar).place(x=270,y=300)

		self.btn4=Button(self.ventana2,text="ELIMINAR",width=10,command=self.eliminar).place(x=390,y=300)

		self.btn5=Button(self.ventana2,text="VOLVER",width=10,command=self.volver).place(x=490,y=300)
		self.btn6=Button(self.ventana2,text="CAMBIO",width=10,command=self.cambio).place(x=30,y=350)		

	def limpiar(self):	
		self.patente.set("")
		self.marca.set("")
		self.año.set("")
		self.carga.set("")
		messagebox.showinfo("MESSAGE",message="Se han limpiado los Campos")	

	def agregar(self):	

		patente= self.patente.get()
		marca= self.combo2.get()
		año=self.combo.get()
		carga=self.carga.get()

		cur = con.cursor()
		#CONSULTA INSERT PARA INSERTAR DATOS 
		cur.execute("INSERT INTO camiones (patente,marca,año,carga) VALUES ('"+(patente)+"','"+(marca)+"','"+str(año)+"','"+(carga)+"')")
		con.commit()
		cur.close()
		self.en1.focus()
		
		messagebox.showinfo("MESSAGE",message="DATOS INGRESADOS")	
		self.patente.set("")
		self.marca.set("")
		self.año.set("")
		self.carga.set("")

	def modificar(self):	

		patente= self.patente.get()
		marca= self.combo2.get()
		año=self.combo.get()
		carga=self.carga.get()

		cur = con.cursor()
		#CONSULTA INSERT PARA INSERTAR DATOS 
		cur.execute("UPDATE camiones SET marca='"+marca+"',año = '"+str(año)+"',carga = '"+carga+"' WHERE patente='"+(patente)+"'")
		con.commit()
		cur.close()
		self.en1.focus()

		messagebox.showinfo("MESSAGE",message="DATOS MODICADOS")	
		self.patente.set("")
		self.marca.set("")
		self.año.set("")
		self.carga.set("")

	def eliminar(self):	

		patente= self.patente.get()
		cur = con.cursor()
		#CONSULTA DELETE PARA ELIMINAR DATOS 
		cur.execute("DELETE FROM camiones  WHERE patente='"+(patente)+"'")
		con.commit()
		cur.close()
		self.en1.focus()
		
		messagebox.showinfo("MESSAGE",message="DATOS ELIMINADOS")	
		self.patente.set("")
		self.marca.set("")
		self.año.set("")
		self.carga.set("")

	def volver(self):
		self.ventana2.destroy()
		form()

	def cambio(self):
		self.ventana2.destroy()
		form3()
###########################TERCER FORMULARIO################################################################
try:
	co = psycopg2.connect("dbname='animales' host='localhost' user='diegoivg98' password='morelloratm2798'")
except:
	print("Hay problemas con la base de datos")
	exit()

class form3():

	def __init__(self):
		self.ventana3=Tk()
		self.ventana3.title("FORMULARIO ANIMALES")
		self.ventana3.geometry("580x400+200+100")

		self.ln1=Label(self.ventana3,text="DIIO: ",font=("Arial",12)).place(x=1,y=10)
		self.diio=IntVar()
		self.en1=Entry(self.ventana3,textvariable=self.diio,takefocus=1)
		self.en1.place(x=125,y=15)
		self.en1.focus()	

		self.ln2=Label(self.ventana3,text="RAZA: ",font=("Arial",12)).place(x=1,y=50)
		self.raza=StringVar()
		self.en2=Entry(self.ventana3,textvariable=self.raza,takefocus=1)
		self.en2.place(x=125,y=55)
		self.en2.focus()	

		self.ln3=Label(self.ventana3,text="EDAD: ",font=("Arial",12)).place(x=1,y=90)
		self.edad=IntVar()
		self.en3=Entry(self.ventana3,textvariable=self.edad,takefocus=1)
		self.en3.place(x=125,y=95)
		self.en3.focus()	

		self.ln4=Label(self.ventana3,text="TIPO: ",font=("Arial",12)).place(x=1,y=130)
		self.tipo=StringVar()
		self.en4=Entry(self.ventana3,textvariable=self.tipo,takefocus=1)
		self.en4.place(x=125,y=135)
		self.en4.focus()	

		self.btn1=Button(self.ventana3,text="LIMPIAR",width=10,command=self.limpiar).place(x=30,y=300)
		self.btn2=Button(self.ventana3,text="AGREGAR",width=10,command=self.agregar).place(x=150,y=300)
		self.btn3=Button(self.ventana3,text="MODIFICAR",width=10,command=self.modificar).place(x=270,y=300)

		self.btn4=Button(self.ventana3,text="ELIMINAR",width=10,command=self.eliminar).place(x=390,y=300)

		self.btn5=Button(self.ventana3,text="VOLVER",width=10,command=self.volver).place(x=490,y=300)

	def limpiar(self):	
		self.diio.set("")
		self.raza.set("")
		self.edad.set("")
		self.tipo.set("")
		messagebox.showinfo("MESSAGE",message="Se han limpiado los Campos")	

	def agregar(self):	

		diio= self.diio.get()
		raza= self.raza.get()
		edad=self.edad.get()
		tipo=self.tipo.get()

		cur = co.cursor()
		#CONSULTA INSERT PARA INSERTAR DATOS 
		cur.execute("INSERT INTO ganado (diio,raza,edad,tipo) VALUES ('"+str(diio)+"','"+(raza)+"','"+str(edad)+"','"+(tipo)+"')")
		co.commit()
		cur.close()
		self.en1.focus()
		
		messagebox.showinfo("MESSAGE",message="DATOS INGRESADOS")	
		self.diio.set("")
		self.raza.set("")
		self.edad.set("")
		self.tipo.set("")

	def modificar(self):

		diio= self.diio.get()
		raza= self.raza.get()
		edad=self.edad.get()
		tipo=self.tipo.get()

		cur = co.cursor()
		#CONSULTA INSERT PARA INSERTAR DATOS 
		cur.execute("UPDATE ganado SET raza='"+raza+"',edad = '"+str(edad)+"',tipo = '"+tipo+"' WHERE diio='"+str(diio)+"'")
		co.commit()
		cur.close()
		self.en1.focus()

		messagebox.showinfo("MESSAGE",message="DATOS MODICADOS")	
		self.diio.set("")
		self.raza.set("")
		self.edad.set("")
		self.tipo.set("")

	def eliminar(self):	

		diio= self.diio.get()
		cur = co.cursor()
		#CONSULTA DELETE PARA ELIMINAR DATOS 
		cur.execute("DELETE FROM ganado  WHERE diio='"+str(diio)+"'")
		co.commit()
		cur.close()
		self.en1.focus()
		
		messagebox.showinfo("MESSAGE",message="DATOS ELIMINADOS")	
		self.diio.set("")
		self.raza.set("")
		self.edad.set("")
		self.tipo.set("")	

	def volver(self):
		self.ventana3.destroy()
		form2()

trabajo=form()