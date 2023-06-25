import tkinter as tk
from tkinter import *
from tkinter import messagebox
from models import *

class MovieViwer(object):
    def __init__(self,manejador):
        fuente_comic_sans = ("Comic Sans MS", 10)
        
        self.__ventana = Tk()
        self.__ventana.title("Cinéfilos Argentinos")
        frame_izquierdo = Frame()
        frame_izquierdo.pack(side="left")
        self.scrollbar = tk.Scrollbar(frame_izquierdo)
        self.listbox = tk.Listbox(frame_izquierdo,font=fuente_comic_sans,foreground='gray35',width=31,height=13,yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=20)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.frame_derecho = Frame() 
        self.frame_derecho.pack(side="right")
        self.frame_derecho.pack()
        
        self.manejadorr = manejador
        self.Lista_Peliculas = manejador.getLista()

        for i in range(len(self.Lista_Peliculas)):
            text = "{}".format(self.Lista_Peliculas[i].getTitulo())
            self.listbox.insert(i,text)

        self.listbox.bind("<Double-Button-1>", self.MostrarDatos)


    def MostrarDatos(self,event):
        seleccion = self.listbox.curselection()
        
        if seleccion:
            i = seleccion[0]
            
            lista_generos = self.manejadorr.Busca_Generos(self.Lista_Peliculas[i].getGeneros())
            cadena = " -- ".join(lista_generos)
            generos = StringVar()
            generos.set(cadena)
            
            titulo = StringVar()
            fecha_lanzamiento = StringVar()
            lenguaje = StringVar()
            fuente_comic_sans = ("Comic Sans MS", 10)
            
            titulo.set(self.Lista_Peliculas[i].getTitulo())
            fecha_lanzamiento.set('Lanzamiento: '+self.Lista_Peliculas[i].getFecha())
            lenguaje.set('Lenguaje: '+self.Lista_Peliculas[i].getLenguaje())
            
            titulo_entry=Entry(self.frame_derecho,textvariable=titulo,state='disabled',width=31,font=fuente_comic_sans,justify='center').grid(row=1,column=1,padx=20,pady=15)
            fecha_entry=Entry(self.frame_derecho,textvariable=fecha_lanzamiento,state='disabled',font=fuente_comic_sans,width=20,justify='center').grid(row=1,column=0,padx=20,pady=15)
            lenguaje_entry=Entry(self.frame_derecho,textvariable=lenguaje,state='disabled',font=fuente_comic_sans,width=20,justify='center').grid(row=1,column=2,padx=20,pady=15)
            
            resumen_text=Text(self.frame_derecho,width=80,height=7)
            resumen_text.grid(row=2,column=0,columnspan=3,pady=20)
            resumen_text.insert(tk.END,self.Lista_Peliculas[i].getResumen())
            resumen_text.config(state='disabled',font=('Comic Sans MS', 10),foreground='gray35')
            
            Entry(self.frame_derecho,textvariable=generos,width=40,state='disabled',justify='center',font=fuente_comic_sans).grid(row=4,column=0,columnspan=3,pady=20)
            
    def Ejecutar(self):
        self.__ventana.mainloop()
        
    
        
        
