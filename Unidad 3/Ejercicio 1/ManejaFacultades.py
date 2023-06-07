from Facultades import Facultad
from Carreras import Carrera
import csv
class ManejaFacultad:
    def __init__(self):
        self.__listafac=[]

    def cargar_archivo(self):
        archivo=open("Facultades.csv",encoding='utf8')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if len(fila)<=5:
                facultadaux=Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                self.__listafac.append(facultadaux)
            else:
                carreraaux=Carrera(int(fila[1]),fila[2],fila[3],fila[4],fila[5])
                facultadaux.agregar_carrera(carreraaux)

    def mostrar_facultades(self):
        for facultad in self.__listafac:
            facultad.mostrar()

    def buscar_facultad(self,cod):
        i=0
        while i<len(self.__listafac) and cod!=self.__listafac[i].get_cod():
            i+=1
        if i>=len(self.__listafac):
            i=False
        return i

    def mostrar_facultad_carreras(self,ind):
        self.__listafac[ind].mostrar_car_dur()
        
    def buscar_carrera(self,nom):
        i=0
        while i<len(self.__listafac) and self.__listafac[i].buscar_carreras(nom)!=True:
            i+=1
        if i<len(self.__listafac):
            print ("Código de Facultad: "+str(self.__listafac[i].get_cod()))
            print ("Localidad de Facultad: "+self.__listafac[i].get_loc())
        else:
            print ("No se encontró la Carrera buscada")
