from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def obtener():
    n1=combo.get()
    s='El valor elegido en el combobox es : '+n1
    messagebox.showinfo("Aviso",message=s)
    n2=chk_state.get()
    if n2==False:
        n2="0"
    n22="el valor elegido en el checkbox es  : "+str(n2)
    messagebox.showinfo("Aviso",message=n2)
    n3="El valor elegido en el radiobutton es : "+str(selected.get())
    messagebox.showinfo("Aviso",message=n3)


ventana=Tk()
ventana.title("ejemplo combobox")
## 500 ancho 300 alto 200 y 100 son para posecionar el form en la pantalla
ventana.geometry("500x300+200+100")

combo = Combobox(ventana)
combo['values']= ("perro", "gato", "laucha", "loro", "pescado", "nada")
combo.place(x=125,y=15) 
combo.current(0) #selecciono el item por defecto

chk_state = BooleanVar() 
chk_state.set(True) #para seleccionar "chequeado"
chk = Checkbutton(ventana, text='Le gustan mas los perros ?', var=chk_state,onvalue = 1, offvalue = 0)
chk.place(x=125,y=55)

lb1=Label(ventana, text="seleccione una opcion : ")
lb1.place(x=123,y=85)

selected = IntVar()
selected.set(1) #para seleccionar la opcion 1
rad1 = Radiobutton(ventana,text='perro', value=1, variable=selected)
rad1.place(x=125,y=105)
rad2 = Radiobutton(ventana,text='gato', value=2, variable=selected)
rad2.place(x=125,y=125)
rad3 = Radiobutton(ventana,text='laucha', value=3, variable=selected)
rad3.place(x=125,y=145)

btn2=Button(ventana,text="obtener",width=10,command=obtener).place(x=150,y=200)
