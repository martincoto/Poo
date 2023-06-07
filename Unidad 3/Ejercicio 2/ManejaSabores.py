from Sabor import Sabor
import csv
class ManejaSabor:
    def __init__(self):
        self.__listasabor=[]
    
    def cargar_sabores(self):
        archivo=open("sabores.csv",encoding='utf8')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            saboraux=Sabor(fila[0],fila[1],fila[2])
            self.__listasabor.append(saboraux)
    
    def get_sabor(self,nomsab):
        i=0
        while i<len(self.__listasabor) and nomsab.upper()!=self.__listasabor[i].get_nom().upper():
            i+=1
        if i<len(self.__listasabor):
            self.__listasabor[i].sumar_pedido()
            return self.__listasabor[i]
        else:
            print ("No se encontró el sabor")

    def mostrar_sabores(self):
        for fila in self.__listasabor:
            fila.mostrar()
    
    def mostrar_mas_pedidos(self):
        listaordenada=sorted(self.__listasabor)
        for i in range (5):
            listaordenada[i].mostrar()