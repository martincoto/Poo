import csv

from Evaluacion import *
class manejadorEvaluaciones():
    __listaE=[]
    def __init__(self):
        self__listaE=[]


    def cargaListaE(self):
        archi=open('evaluacion.csv',encoding='utf8')
        reader=csv.reader(archi,delimiter=';')
        
        for fila in reader:
            aux=[float(fila[2]),float(fila[3]),float(fila[4])]
            unaEvaluacion=Evaluacion(fila[0],fila[1],aux)
            self.__listaE.append(unaEvaluacion)
    
    def mostrarLista(self):
        for i in range(len(self.__listaE)):
            self.__listaE[i].mostrarDatos()
            #print("a")
    def guardaLista(self):
        return self.__listaE
