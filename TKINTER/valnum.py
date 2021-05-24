from tkinter import ttk
import tkinter as tk
 
def is_valid_char(char):
    return char in "0123456789."
 
root = tk.Tk()
validatecommand = root.register(is_valid_char)
entry = ttk.Entry(root, validate="key", validatecommand=(validatecommand, "%S"))
entry.pack()
root.mainloop()