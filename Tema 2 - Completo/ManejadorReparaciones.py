import csv
from Reparacion import *

class ManejadorReparaciones():
    __listar=[]
    def __init__(self):
        __listar=[]

    def CargarReparaciones(self):
        archivo=open('reparaciones.csv')
        reader=csv.reader(archivo,delimiter=';')    
        saltearFila=True 
        for fila in reader:
            if saltearFila:
                saltearFila=False
            else:
                unaReparacion=Reparacion(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__listar.append(unaReparacion)
    def getListaR(self):
        return self.__listar
                
    def mostrarDatosReparacion(self,j):
        print("{:<35}${:<15.2f}${:<15.2f}${:.2f}".format(self.__listar[j].getReparacion(),float(self.__listar[j].getRPrecio()),float(self.__listar[j].getManoPrecio()),float(self.__listar[j].getRPrecio())+float(self.__listar[j].getManoPrecio())))
    
    def subtotal(self,j):
        subtotales=float(self.__listar[j].getRPrecio())+float(self.__listar[j].getManoPrecio())
        return subtotales
    
    