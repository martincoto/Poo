from TallerCapacitacion import TallerCap
import csv
class ManejaTaller:
    def __init__(self):
        self.__listataller=[]
        
    def cargar_talleres(self):
        archivo=open("Talleres.csv",encoding="utf8")
        reader=csv.reader(archivo,delimiter=';')
        for i,fila in enumerate(reader):
            if i!=0:
                talleraux=TallerCap(fila[0],fila[1],int(fila[2]),fila[3])
                self.__listataller.append(talleraux)
        
    def mostrar_talleres(self):
        for taller in self.__listataller:
            print (taller)
    
    def buscar_taller(self,nom):
        i=0
        while i<len(self.__listataller) and nom.upper()!=self.__listataller[i].get_nom().upper():
            i+=1
        if i<len(self.__listataller):
            self.__listataller[i].restar_vacante()
            c=self.__listataller[i]
        else:
            c=False
        return c
