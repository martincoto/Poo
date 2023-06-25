from tkinter import *
class aplicacion():
    def __init__(self):
        
        self.__ventana=Tk()
        self.__ventana.title('Calculadora IPC')
        mainframe=Frame()
        self.__total=StringVar()
        Label(mainframe,text="Item").grid(row=1,column=1,padx=10,pady=10)
        Label(mainframe,text="Cantidad").grid(row=1,column=2,padx=10,pady=10)
        Label(mainframe,text="Precio Año Base").grid(row=1,column=3,padx=10,pady=10)
        Label(mainframe,text="Precio Año Actual").grid(row=1,column=4,padx=10,pady=10)
        Label(mainframe,text="Vestimienta").grid(row=2,column=1,padx=10,pady=10)
        Label(mainframe,text="Alimentos").grid(row=3,column=1,padx=10,pady=10)
        Label(mainframe,text="Educación").grid(row=4,column=1,padx=10,pady=10)
        
        self.cant1=Entry(mainframe,relief='groove',borderwidth=2)
        self.cant1.grid(row=2,column=2,padx=10,pady=10)
        
        self.cant2=Entry(mainframe,relief='groove',borderwidth=2)
        self.cant2.grid(row=3,column=2,padx=10,pady=10)
        self.cant3=Entry(mainframe,relief='groove',borderwidth=2)
        self.cant3.grid(row=4,column=2,padx=10,pady=10)
        self.pBase1=Entry(mainframe,relief='groove',borderwidth=2)
        self.pBase1.grid(row=2,column=3,padx=10,pady=10)
        self.pBase2=Entry(mainframe,relief='groove',borderwidth=2)
        self.pBase2.grid(row=3,column=3,padx=10,pady=10)
        
        self.pBase3=Entry(mainframe,relief='groove',borderwidth=2)
        self.pBase3.grid(row=4,column=3,padx=10,pady=10)
        self.pActual1=Entry(mainframe,relief='groove',borderwidth=2)
        self.pActual1.grid(row=2,column=4,padx=10,pady=10)
        self.pActual2=Entry(mainframe,relief='groove',borderwidth=2)
        self.pActual2.grid(row=3,column=4,padx=10,pady=10)
        self.pActual3=Entry(mainframe,relief='groove',borderwidth=2)
        self.pActual3.grid(row=4,column=4,padx=10,pady=10)
        mainframe.pack()
        midFrame=Frame()
        Button(midFrame,text='Calcular IPC',command=self.CalculoIPC,relief='groove',borderwidth=2,bg='Gray75').grid(row=1,column=1, padx=80,pady=10)
        Button(midFrame,text='Salir',command=quit,relief='groove',borderwidth=2,bg='Gray75').grid(row=1,column=2,padx=80,pady=10,sticky=W)
        midFrame.pack()
        bottomFrame=Frame()
        Label(bottomFrame,text='IPC %').grid(row=1,column=1, padx=0,pady=10)
        Label(bottomFrame,textvariable=self.__total).grid(row=1,column=2, padx=20,pady=10,sticky='W')
        Label(bottomFrame,text='').grid(row=2,column=2, padx=200,pady=10)
        bottomFrame.pack()
        self.__ventana.mainloop()
        
    def CalculoIPC(self):
        costoActual=float(self.cant1.get())*float(self.pActual1.get())+float(self.cant2.get())*float(self.pActual2.get())+float(self.cant3.get())*float(self.pActual3.get())
        costoBase=float(self.cant1.get())*float(self.pBase1.get())+float(self.cant2.get())*float(self.pBase2.get())+float(self.cant3.get())*float(self.pBase3.get())
        self.__total.set((costoActual/costoBase)*100)
        

if __name__=='__main__':
    Interfaz=aplicacion()
    