from tkinter import ttk
import tkinter as tk

class suma:
	def __init__(self):
		self.ventana=tk.Tk()
		self.ventana.geometry("300x300")

		self.var = tk.StringVar()

		self.e1 = ttk.Entry(self.ventana)
		self.e1.pack()

		self.e2 = ttk.Entry(self.ventana)
		self.e2.pack()

		self.b1 = tk.Button(self.ventana,text="SUMAR", command=self.sumar)
		self.b1.pack()

		self.res = tk.Label(self.ventana,padx=30,pady=2,bg="white",textvariable=self.var)
		self.res.pack()

		self.ventana.mainloop()        

	def sumar(self):
		self.suma = float(self.e1.get()) + float(self.e2.get())
		return self.var.set(self.suma)

aplicacion1=suma() 