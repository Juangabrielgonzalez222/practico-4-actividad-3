import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk,font,messagebox
from datetime import datetime
class App():
    __ventana=None
    __hora=None
    __lista=[]
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.resizable(0,0)
        for i in range(3):
            self.__lista.append([])
        self.__ventana.title("Cotizaciones del dólar")
        self.contenedor1=ttk.LabelFrame(self.__ventana,text="Nombre:")
        self.contenedor1.grid(column=0,row=0,sticky="nswe",padx=5,ipadx=10,pady=10)
        self.contenedor2=ttk.LabelFrame(self.__ventana,text="Compra:")
        self.contenedor2.grid(column=1,row=0,sticky="nswe",padx=5,ipadx=10,pady=10)
        self.contenedor3=ttk.LabelFrame(self.__ventana,text="Venta:")
        self.contenedor3.grid(column=2,row=0,sticky="nswe",padx=5,ipadx=10,pady=10)
        self.contenedor4=tk.Frame(self.__ventana)
        self.contenedor4.grid(column=3,row=0,sticky="nswe",padx=5,ipadx=10,pady=15)
        ult=ttk.Label(self.contenedor4,text="Última")
        ult.grid(column=3,row=1)
        act=ttk.Label(self.contenedor4,text="Actualización:")
        act.grid(column=3,row=2)
        self.__hora=StringVar()
        self.calculaHora()
        self.hora=tk.Label(self.contenedor4,textvariable=self.__hora)
        self.hora.grid(column=3,row=3)
        self.boton=ttk.Button(self.contenedor4,text="Actualizar",command=self.actualizar)
        self.boton.grid(column=3,row=4,sticky="sw",pady=(90,0))
        try:
            respuesta=requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
            dic=respuesta.json()
            x=0
            for linea in dic:
                if(linea["casa"]["nombre"].count("Dolar")!=0):
                    nombre=linea["casa"]["nombre"].replace("Dolar","Dólar")
                    nom=tk.Label(self.contenedor1,text=nombre)
                    nom.grid(column=0,row=x,sticky="e")
                    self.__lista[0].append(nom)
                    compra=tk.Label(self.contenedor2,text=linea["casa"]["compra"])
                    compra.grid(column=1,row=x,sticky="we",padx=(15,0))
                    self.__lista[1].append(compra)
                    venta=tk.Label(self.contenedor3,text=linea["casa"]["venta"])
                    venta.grid(column=2,row=x,sticky="ew",padx=(15,0))
                    self.__lista[2].append(venta)
                    x+=1
        except:
            messagebox.showerror(title="Error en la conexion",message="Hubo un error en la conexion a la api.")
        self.__ventana.mainloop()
    def calculaHora(self):
        hora=datetime.now()
        self.__hora.set(str(hora.hour)+":"+str(hora.minute))
    def actualizar(self):
        self.calculaHora()
        try:
            respuesta=requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
            dic=respuesta.json()
            i=0
            for elemento in dic:
                if(elemento["casa"]["nombre"].count("Dolar")!=0):
                    self.__lista[1][i].config(text=elemento["casa"]["compra"])
                    self.__lista[2][i].config(text=elemento["casa"]["venta"])
                    i+=1
        except:
            messagebox.showerror(title="Error en la conexion",message=self.__lista)