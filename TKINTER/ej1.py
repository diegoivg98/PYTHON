from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

def obtener():
	txt1="RUT : "+str(rut.get())
	messagebox.showinfo("Aviso",message=txt1) #RUT

	txt2="NOMBRE: "+str(nombre.get())
	messagebox.showinfo("Aviso",message=txt2) #NOMBRE

	txt3="APELLIDO: "+str(apellido.get())
	messagebox.showinfo("Aviso",message=txt3) #APELLIDO

	txt4="EDAD: "+str(edad.get())
	messagebox.showinfo("Aviso",message=txt4) #EDAD

	n1=combo.get()
	n2=comb2.get()
	n3=comb3.get()
	s='Fecha de nacimiento : '+n1+'/'+n2+'/'+n3 #FECHA NACIMIENTO
	messagebox.showinfo("Aviso",message=s)

	n3="El valor elegido en el radiobutton es : "+str(selected.get()) #SEXO
	messagebox.showinfo("Aviso",message=n3)

	n4=comb4.get()
	e='Estado Civil : '+n4 #FECHA NACIMIENTO
	messagebox.showinfo("Aviso",message=e)

	txt5="N° de hijos: "+str(nhijos.get())
	messagebox.showinfo("Aviso",message=txt5) #NUMERO DE HIJOS


def limpiar():
	#BOTON LIMPIAR TEXTBOX
	rut.set("")
	nombre.set("")
	apellido.set("")
	edad.set("")
	nhijos.set("")
	
	messagebox.showinfo("Nota",message="Se han limpiado los Campos")
	en1.focus()

ventana=Tk()
ventana.title("FORMULARIO")
ventana.geometry("1200x700+200+100") 

#font: Arial, gothic, mincho, Times New Roman, Symbol

ln1=Label(text="Ingrese su rut: ",font=("Arial",12)).place(x=1,y=10)
rut=StringVar()
en1=Entry(ventana,textvariable=rut,takefocus=1)
en1.place(x=125,y=15)
en1.focus()

ln2=Label(text="Ingrese ambos nombres: ",font=("Arial",12)).place(x=1,y=50)
nombre=StringVar()
en2=Entry(ventana,textvariable=nombre).place(x=180,y=55)

ln3=Label(text="Ingrese apellidos: ",font=("Arial",12)).place(x=1,y=90)
apellido=StringVar()
en3=Entry(ventana,textvariable=apellido).place(x=130,y=90)

ln4=Label(text="Ingrese edad: ",font=("Arial",12)).place(x=1,y=130)
edad=StringVar()
en3=Entry(ventana,textvariable=edad).place(x=125,y=130)

ln5=Label(text="Ingrese fecha de nacimiento: ",font=("Arial",12)).place(x=1,y=170)
combo = Combobox(ventana,state='readonly',width=5)
combo['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,23,25,26,27,28,29,30,31)
combo.place(x=210,y=170)
combo.current(0) 

comb2 = Combobox(ventana,state='readonly',width=5)
comb2['values']= (1,2,3,4,5,6,7,8,9,10,11,12) 
comb2.place(x=270,y=170) 
comb2.current(0) 

comb3 = Combobox(ventana,state='readonly',width=6)
comb3['values']= ("1960", "1961", "1962", "1963", "1964", "1965", "1965", "1966", "1967", "1968", "1969", "1970",
	"1971", "1972", "1973", "1974", "1975", "1976","1977", "1978", "1979", "1980",
	"1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", 
	"1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", 
	"2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", 
	"2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019")
comb3.place(x=330,y=170) 
comb3.current(0) 


ln6=Label(text="Sexo: ",font=("Arial",12)).place(x=1,y=210)
selected = IntVar()
selected.set(1) #para seleccionar la opcion 1
rad1 = Radiobutton(ventana,text='Masculino', value=1, variable=selected)
rad1.place(x=50,y=197)
rad2 = Radiobutton(ventana,text='Femenino', value=2, variable=selected)
rad2.place(x=50,y=215)

ln7=Label(text="Estado Civil: ",font=("Arial",12)).place(x=1,y=250)
comb4 = Combobox(ventana,state='readonly',width=10)
comb4['values']= ("Soltero/a","Casado/a","Viudo/a")
comb4.place(x=105,y=250) 
comb4.current(0) 

ln8=Label(text="Numero de hijos/as: ",font=("Arial",12)).place(x=1,y=290)
nhijos=StringVar()
en4=Entry(ventana,textvariable=nhijos).place(x=145,y=290)

ln9=Label(text="Es socio del glorioso Rangers de  Talca ?: ",font=("Arial",12)).place(x=1,y=330)
selected2 = IntVar()
selected2.set(1) #para seleccionar la opcion 1
rad3 = Radiobutton(ventana,text='Si', value=1, variable=selected2)
rad3.place(x=305,y=325)
rad4 = Radiobutton(ventana,text='No', value=2, variable=selected2)
rad4.place(x=305,y=345)

btn2=Button(ventana,text="OBTENER",bg="red", fg="white", width=10,command=obtener).place(x=150,y=400)
btn1=Button(ventana,text="LIMPIAR",bg="blue", fg="white",width=10,command=limpiar).place(x=250,y=400)

ventana.mainloop()