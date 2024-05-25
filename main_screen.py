# Importando tkinter para crear la ventana principal
from tkinter import *
from tkinter import ttk
# Importando las pantallas del py file caesar_cypher_screens
import caesar_cypher_screens as caesar

# Creando root como un TK element, no resizable y con título Menú
root=Tk()
root.resizable(False,False)
root.title('Menú')
# Crea un form con ttk.Frame dentro del root con padding=10 y se inicializa el formato grid para organizar los elementos de forma sencilla
frm = ttk.Frame(root,padding=10)
frm.grid()
# Se ponen 2 labels como información y 2 botones que llaman funciones del file caesar_cypher_screens
ttk.Label(frm,text='Menú de selección').grid(column=1,row=1)
ttk.Label(frm,text='Selecciona el ejercicio que quieres visualizar').grid(column=1,row=2)
ttk.Button(frm, text='Ejercicio1',command=caesar.ejercicio1).grid(column=1,row=3)
ttk.Button(frm, text='Ejercicio2',command=caesar.ejercicio2).grid(column=1,row=4)
# Se muestra la pantalla root
root.mainloop()