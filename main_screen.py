from tkinter import *
from tkinter import ttk
import cypher

def ejercicio2():
    def encriptado(label,texto,key):
        try:
            nuevo_texto=cypher.encrypt(texto,int(key))
            label.config(text=nuevo_texto)
        except:
            label.config(text='Por favor revise los campos')

    def desencriptado(label,texto,key):
        try:
            nuevo_texto=cypher.decrypt(texto,int(key))
            label.config(text=nuevo_texto)
        except:
            label.config(text='Por favor revise los campos')

    caesar=Toplevel()
    caesar.resizable(False,False)
    caesar.title('Cesar')
    frm = ttk.Frame(caesar,padding=10)
    frm.grid()
    ttk.Label(frm,text='Texto Original:').grid(column=1,row=1)
    texto=ttk.Entry(frm)
    texto.grid(column=2,row=1)
    ttk.Label(frm,text='Llave de Cifrado:').grid(column=1,row=2)
    clave=ttk.Entry(frm)
    clave.grid(column=2,row=2)
    ttk.Label(frm,text='Texto Generado:').grid(column=1,row=4)
    resultado=ttk.Label(frm)
    resultado.grid(column=2,row=4)
    ttk.Button(frm, text='Cifrar', command= lambda: encriptado(resultado,texto.get(),clave.get())).grid(column=1,row=3)
    ttk.Button(frm, text='Descifrar', command= lambda: desencriptado(resultado,texto.get(),clave.get())).grid(column=2,row=3)

root=Tk()
root.resizable(False,False)
root.title('Menú')
frm = ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm,text='Menú de selección').grid(column=1,row=1)
ttk.Label(frm,text='Selecciona el ejercicio que quieres visualizar').grid(column=1,row=2)
ttk.Button(frm, text='Ejercicio1').grid(column=1,row=3)
ttk.Button(frm, text='Ejercicio2',command=ejercicio2).grid(column=1,row=4)
root.mainloop()