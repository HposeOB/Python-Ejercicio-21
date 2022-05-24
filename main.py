
import tkinter as tk
from tkinter import *


def reset():
    etiqueta.config(text="")
    valor.set(None)

def nombre():
    etiqueta.config(text=valor.get())

ventana = tk.Tk()
ventana.title("Aplicacion Open Bootcamp")
ventana.config(width=400, height=300)
etiqueta = Label(ventana)
valor = tk.StringVar()

opcion1 = tk.Radiobutton(ventana, text='A', variable=valor, value="A", command=nombre)
opcion2 = tk.Radiobutton(ventana, text='B', variable=valor, value="B", command=nombre)
opcion3 = tk.Radiobutton(ventana, text='C', variable=valor, value="C", command=nombre)

reset = tk.Button(ventana, text="Reset", command=reset)

opcion1.grid(column=0, row=0)
opcion2.grid(column=0, row=1)
opcion3.grid(column=0, row=2)
reset.grid(column=1, row=0)
etiqueta.grid(column=1, row=1)


ventana.mainloop()