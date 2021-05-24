from tkinter import ttk
import tkinter as tk

def obtener():
  if combo.get()=='suma':
    suma = float(e1.get()) + float(e2.get())
    return var.set(suma)

  if combo.get()=='resta':
    resta = float(e1.get()) - float(e2.get())
    return var.set(resta)

  if combo.get()=='multiplicar':
    mult= float(e1.get()) * float(e2.get())
    return var.set(mult)

  if combo.get()=='dividir':
    div = float(e1.get()) / float(e2.get())
    return var.set(div)

#validar campo numerico y punto para decimales
def is_valid_char(char):
    return char in "0123456789."

ventana = tk.Tk()
ventana.geometry("300x300")
var = tk.StringVar()
validatecommand = ventana.register(is_valid_char)

e1 = ttk.Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"))
e1.pack()
e2 = ttk.Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"))
e2.pack()

combo = ttk.Combobox(ventana)
combo.place(x=50, y=100)
combo['values'] = ('suma','resta','multiplicar','dividir')
combo.current()

boton = ttk.Button(ventana,command=obtener,text="calcular").place(x=80, y=200)

res = tk.Label(ventana,padx=30,pady=2,bg="white",textvariable=var)
res.pack()
ventana.mainloop()