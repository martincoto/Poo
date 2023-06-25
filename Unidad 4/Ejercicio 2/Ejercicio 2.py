from tkinter import *
from tkinter.ttk import *

class Application():
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("280x240")
        self.__ventana.title('Cálculo de IVA')
        self.tipoIva=IntVar()
        self.__cant=StringVar()
        self.__total=StringVar()

        estilo = Style()
        estilo.configure('botonRojo.TButton', background='#F8CECC', relief='solid', borderwidth=2, bordercolor='#B85450')
        estilo.configure('botonCalcular.TButton', background='#D5E8D4', relief='solid', borderwidth=2, bordercolor='black')
        estilo.configure('label1.TLabel', background='#DAE8FC', relief='solid', borderwidth=2, bordercolor='#6C8EBF')

        topframe = Frame(self.__ventana)
        Label(topframe, text='Cálculo de IVA', style='label1.TLabel').grid(row=1, column=1, ipady=10, ipadx=75)
        topframe.pack()

        self.mainframe = Frame(self.__ventana)
        Label(self.mainframe, text='Precio sin IVA').grid(row=1, column=1, padx=20, sticky='W', ipady=10, ipadx=10)
        self.precioSI = Entry(self.mainframe)
        self.precioSI.grid(row=1, column=2, pady=30)

        
        Radiobutton(self.mainframe, text='IVA 21%', value=1,variable=self.tipoIva).grid(row=2, column=1, columnspan=1, sticky='w', padx=35)
        Radiobutton(self.mainframe, text='IVA 10.5%', value=0,variable=self.tipoIva).grid(row=3, column=1, columnspan=1, sticky='w', padx=35)

        calcular_button = Button(self.mainframe, text='Calcular',command=self.calculoIva)
        calcular_button.configure(style='botonCalcular.TButton')
        calcular_button.grid(row=6, column=1)

        salir_button = Button(self.mainframe, text='Salir', command=quit)
        salir_button.configure(style='botonRojo.TButton')
        salir_button.grid(row=6, column=2)

        self.mainframe.pack()
        self.__ventana.mainloop()
    
    def calculoIva(self):
        if self.tipoIva.get()==0:
            self.__total.set(float(self.precioSI.get())*10.5/10)
            self.__cant.set('10.5')
            
            Label(self.mainframe, text='IVA').grid(row=4, column=1, padx=10)
            self.precioIVA = Label(self.mainframe,textvariable=self.__cant,style="label1.TLabel")
            self.precioIVA.grid(row=4, column=2,sticky='WE')

            Label(self.mainframe, text='Precio con IVA').grid(row=5, column=1, padx=10)
            self.precioConIVA = Label(self.mainframe, textvariable=self.__total, style="label1.TLabel")
            self.precioConIVA.grid(row=5, column=2,sticky='WE')
            
        else:
            self.__total.set(float(self.precioSI.get())*21/100)
            self.__cant.set('21')
            
            Label(self.mainframe, text='IVA').grid(row=4, column=1, padx=10)
            self.precioIVA = Label(self.mainframe,textvariable=self.__cant,style="label1.TLabel")
            self.precioIVA.grid(row=4, column=2,sticky='WE')

            Label(self.mainframe, text='Precio con IVA').grid(row=5, column=1, padx=10)
            self.precioConIVA = Label(self.mainframe, textvariable=self.__total, style="label1.TLabel")
            self.precioConIVA.grid(row=5, column=2,sticky='WE')
            

if __name__ == '__main__':
    interfaz = Application()
