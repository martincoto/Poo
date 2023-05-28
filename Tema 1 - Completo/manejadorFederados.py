import csv

from Federados import *
class manejadorFederados():
    __listaF=[]
    def __init__(self):
        self.__listaF=[]


    def cargaLista(self):
        archi=open('federados.csv',encoding='utf8')
        reader=csv.reader(archi,delimiter=';')
        for fila in reader:
            unFederado=Federados(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__listaF.append(unFederado)
    
    def mostrarLista(self):
        for i in range(len(self.__listaF)):
            self.__listaF[i].mostrarDatos()

#        1)Leer un estilo y una edad y listar apellido, nombre y DNI de cada patinador que 
#        participó en el estilo dado

    def patinajeEstilo(self,listaE):
        i=0
        estilo=input("Ingresa un Estilo: ")
        edad=input("Ingresa una Edad: ")
        while i<(len(self.__listaF)):
            if ((self.__listaF[i].getEdad()==edad) and (listaE[i].getEstilo()==estilo)):
                self.__listaF[i].mostrarDatos1()
            i=i+1
        
        input("--------precione enter para volver al menu---------")
    
#    2)Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador 
 #       que obtuvo el mayor puntaje en la evaluación. 
  #      Regla de negocio: El puntaje es el promedio de las 3 valoraciones dadas por los 
   #     jueces. Además, para resolver esta funcionalidad, el analista le solicita que 
    #    sobrecargueel operador “>”.
        
    def mayorPuntaje(self,listaE):
        mayor=0
        for i in range(len(self.__listaF)):
            mayor=listaE[i].__gt__(mayor)
        j=0
        while j<(len(self.__listaF)):
            if mayor==listaE[j].calculoProm():
                estilo=listaE[j].getEstilo()
                self.__listaF[j].mostrarDatos2(estilo)
            j=j+1
        input("--------precione enter para volver al menu---------")
    
    def listarPatinadores(self,listaE):
        print("Los de Escuela son: \n")
        for i in range(len(self.__listaF)):
            if (listaE[i].getEstilo())=='E':
                self.__listaF[i].mostrarDatos()
        print("\nLos de Estilo Libre son: \n")
        for j in range(len(self.__listaF)):
            if (listaE[j].getEstilo())=='L':
                self.__listaF[j].mostrarDatos()
        input("--------precione enter para volver al menu---------")
    
    def puntuacionP(self,listaE):
        unDni=input("Ingresa un DNI: ")
        unEstilo=input("Igresa un estilo: ").upper()
        i=0
        while i<len(self.__listaF):
            if (listaE[i].getEstilo()==unEstilo)and(self.__listaF[i].getDni()==unDni):
                listaE[i].mostrarDatos4()
                i==len(self.__listaF)
            i=i+1
        
        input("--------precione enter para volver al menu---------")
                
                
        
            
        
        
    
