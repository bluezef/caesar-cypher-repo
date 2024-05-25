# Importando tkinter para crear las ventanas
from tkinter import *
from tkinter import ttk
# Se importa cypher para llamar las funciones que permiten encriptar y desencriptar
import cypher
# Se importa base64 para encriptar y desencritar hacia y desde base64 fácilmente
import base64 as b64

# Se define una errorfunction que muestra una pantalla en caso ocurra un error en el programa
def errorfunction():   
    error=Toplevel()
    error.resizable(False,False)
    error.title('Error')
    frm = ttk.Frame(error,padding=10)
    frm.grid()
    ttk.Label(frm,text=('Ocurrió un error, revise que los campos estén debidamente completados.')).grid(column=1,row=1)

def encriptado(resultado, bin, hex, base64,texto,key):
        """Se define una función llamada encriptado para el uso del ejercicio 1 con 6 parámetros
        resultado: La label en donde se mostrará el nuevo texto generado por la encriptación
        bin: La label donde se mostrará el texto encriptado en binario
        hex: La label donde se mostrará el texto encriptado en hexadecimal
        base64: La label donde se mostrará el texto encriptado en base64
        texto, key: Elementos necesarios para la función encrypt (texto a encriptar y clave)"""
        try:
            # Llama a la función encrypt del documento cypher y almacena el resultado en una variable llamada nuevo_texto
            nuevo_texto=cypher.encrypt(texto,int(key))
            # Setea el texto de la label resultado para que refleje el texto generado
            resultado.config(text=nuevo_texto)
            # Hace la conversión a binario usando la función format y la asigna al texto en la label bin
            bin.config(text=''.join(format(ord(x),'b') for x in nuevo_texto))
            # Hace la conversión a hex usando la función format y la asigna al texto en la label hex
            hex.config(text=''.join(format(ord(x),'x') for x in nuevo_texto))
            # Hace la conversión a base64 usando la función b64encode y la asigna al texto en la label base64
            base64.config(text=b64.b64encode(nuevo_texto.encode()))
        except:
            # Si hay un error llama a la errorfunction
            errorfunction()
            
            
def desencriptado(resultado,texto_base64,key):
        """Se define una función llamada encriptado para el uso del ejercicio 2 con 3 parámetros
        resultado: La label en donde se mostrará el nuevo texto generado por la desencriptación
        texto_base64: Texto a desencriptar en formato base64
        key: Elemento para la función decrypt (clave)"""
        try:
            # Desencripta de base64 a texto ASCII como primer paso y lo almacena en la función texto
            texto=b64.b64decode(texto_base64).decode()
            # Se llama a la función decrypt y se le pasan los valores texto y key
            nuevo_texto=cypher.decrypt(texto,int(key))
            # Se muestra el nuevo texto desencriptado en la label resultado
            resultado.config(text=nuevo_texto)
        except:
            errorfunction()

def ejercicio1():
    """Se define una función ejercicio1 que muestra la pantalla para el ejercicio 1, creando un form a nivel Toplevel(), es decir sobre la ventana principal
    Cuenta con:
    5 labels que especifican lo que se necesita ingresar o lo que se mostrará
    2 Entries que reciben el texto a encriptar y la llave de encriptación
    3 labels que sirven para luego cambiar su texto a los resultados
    1 botón que llama la función encriptado al presionarse"""   
    caesar=Toplevel()
    caesar.resizable(False,False)
    caesar.title('Ejercicio 1')
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
    ttk.Label(frm,text='Texto Generado Binario:').grid(column=1,row=5)
    bin=ttk.Label(frm)
    bin.grid(column=2,row=5)
    ttk.Label(frm,text='Texto Generado Hexadecimal:').grid(column=1,row=6)
    hex=ttk.Label(frm)
    hex.grid(column=2,row=6)
    ttk.Label(frm,text='Texto Generado Base64:').grid(column=1,row=7)
    base64=ttk.Label(frm)
    base64.grid(column=2,row=7)
    ttk.Button(frm, text='Cifrar', command= lambda: encriptado(resultado,bin,hex,base64,texto.get(),clave.get())).grid(column=1,row=3)

def ejercicio2():
    """Se define una función ejercicio1 que muestra la pantalla para el ejercicio 2, creando un form a nivel Toplevel(), es decir sobre la ventana principal
    Cuenta con:
    3 labels que especifican lo que se necesita ingresar o lo que se mostrará
    2 Entries que reciben el texto a encriptar en base64 y la llave de encriptación
    1 label que sirve para luego cambiar su texto al resultado
    1 botón que llama la función desencriptado al presionarse""" 
    caesar=Toplevel()
    caesar.resizable(False,False)
    caesar.title('Ejercicio 2')
    frm = ttk.Frame(caesar,padding=10)
    frm.grid()
    ttk.Label(frm,text='Texto Original en Base64:').grid(column=1,row=1)
    texto=ttk.Entry(frm)
    texto.grid(column=2,row=1)
    ttk.Label(frm,text='Llave de Cifrado:').grid(column=1,row=2)
    clave=ttk.Entry(frm)
    clave.grid(column=2,row=2)
    ttk.Label(frm,text='Texto Descifrado:').grid(column=1,row=4)
    resultado=ttk.Label(frm)
    resultado.grid(column=2,row=4)
    ttk.Button(frm, text='Descifrar', command= lambda: desencriptado(resultado,texto.get(),clave.get())).grid(column=2,row=3)