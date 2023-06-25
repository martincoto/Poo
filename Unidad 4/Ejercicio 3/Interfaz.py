import tkinter as tk
from tkinter import ttk,messagebox
class Aplicacion():
    def __init__(self,cotizacion):
        self.__ventana= tk.Tk()
        self.__cotiz=cotizacion
        self.__dolar=tk.StringVar()
        self.__pesos=tk.StringVar()
        self.__ventana.title("Conversor de moneda")
        self.__ventana.config(borderwidth=2,relief='sunken')
        eq_label=ttk.Label(self.__ventana,text='es equivalente a')
        eq_label.grid(row=1,column=0,columnspan=2)
        self.dolar_entry=ttk.Entry(self.__ventana,textvariable=self.__dolar,width=8)
        self.dolar_entry.grid(row=0,column=2,padx=10)
        dolar_label=ttk.Label(self.__ventana,text='dólares')
        dolar_label.grid(row=0,column=3,sticky='w')
        pesos_label=ttk.Label(self.__ventana,text='pesos')
        pesos_label.grid(row=1,column=3,sticky='w')
        cambio_label=ttk.Label(self.__ventana,textvariable=self.__pesos)
        cambio_label.grid(row=1,column=2)
        salir_button=ttk.Button(self.__ventana,text='Salir',command=self.__ventana.destroy)
        salir_button.grid(row=2,column=3)
        self.dolar_entry.bind("<KeyRelease>",self.calcular_cambio)
        self.__ventana.config(padx=15,pady=15)
        self.__ventana.mainloop()
    
    def calcular_cambio(self,event):
        try:
            dolar=float(self.__dolar.get())
            pesos=self.__cotiz*dolar
            self.__pesos.set(self.__cotiz*dolar)
        except ValueError:
            messagebox.showerror(title='Error de valor', message='Debe ingresar valores numéricos en el precio')
            self.dolar_entry.delete("0","end")
