from Nodo import Nodo
from PersonalApoyo import PersonalApoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
class ListaAgente:
    __comienzo=Nodo
    def __init__(self):
        self.__comienzo=None
    
    def insertar_agente(self,posicion,agente):
        if posicion!=0:
            aux=self.__comienzo
            for i in range(posicion):
                anterior=aux
                aux=aux.getSiguiente()
            nuevonodo=Nodo(agente)
            anterior.setSiguiente(nuevonodo)
            nuevonodo.setSiguiente(aux)
        else:
            self.agregar_agente(agente)
        
    def agregar_agente(self,agente):
        nodo=Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    
    def mostrar_objeto_posicion(self,posicion):
        aux=self.__comienzo
        for i in range(posicion):
            aux=aux.getSiguiente()
        if isinstance(aux.getAgente(),PersonalApoyo):
            print ("El agente en esa posición es de Personal de Apoyo")
        elif isinstance(aux.getAgente(),Docente):
            if isinstance(aux.getAgente(),DocenteInvestigador):
                print ("El agente en esa posición es de Docente-Investigador")
            else:
                print ("El agente en esa posición es de Docente")
        elif isinstance(aux.getAgente(),Investigador):
            print ("El agente en esa posición es de Investigador")
    
    def listado_carrera(self,carrera):
        aux=self.__comienzo
        lista_carre=[]
        while aux!=None:
            if isinstance(aux.getAgente(),DocenteInvestigador):
                if carrera.upper()==aux.getAgente().get_carrera().upper():
                    lista_carre.append(aux.getAgente())
            aux=aux.getSiguiente()
        lista_carre.sort(key=lambda agente: agente.get_nom())
        print ("Lista de agentes:")
        for agente in lista_carre:
            print(agente)
    
    def contar_agentes(self,area):
        aux=self.__comienzo
        contador=[0,0]
        while aux!=None:
            if isinstance(aux.getAgente(),DocenteInvestigador):
                if aux.getAgente().get_area().upper()==area.upper():
                    contador[0]+=1
            elif isinstance(aux.getAgente(),Investigador):
                if aux.getAgente().get_area().upper()==area.upper():
                    contador[1]+=1
            aux=aux.getSiguiente()
        print ("La cantidad de Docentes-Investigadores en esa área es de: {}\nLa cantidad de Investigadores en esa área es de: {}".format(contador[0],contador[1]))
    
    def generar_listado(self):
        aux=self.__comienzo
        listado_ord=[]
        while aux!=None:
            listado_ord.append(aux.getAgente())
            aux=aux.getSiguiente()
        listado_ord.sort()
        print ("Listado de agentes:")
        for agente in listado_ord:
            if isinstance(agente,PersonalApoyo):
                print ("Personal de Apoyo")
            elif isinstance(agente,Docente):
                if isinstance(agente,DocenteInvestigador):
                    print ("Docente-Investigador")
                else:
                    print ("Docente")
            elif isinstance(agente,Investigador):
                print ("Investigador")
            agente.mostrar_datos_sueldo()
    
    def mostrar_categoria(self,categoria):
        aux=self.__comienzo
        importe=0
        print ("Listado de Docentes-Investigadores:")
        while aux!=None:
            if isinstance(aux.getAgente(),DocenteInvestigador):
                if aux.getAgente().get_categoria().upper()==categoria.upper():
                    aux.getAgente().mostrar_nom_ap()
                    print ("Importe extra por docencia: {}".format(aux.getAgente().get_impextra()))
                    importe+=aux.getAgente().get_impextra()
            aux=aux.getSiguiente()
        print ("Total de dinero a solicitar: {}".format(importe))
        
    def mostrar_lista(self):
        aux=self.__comienzo
        while aux!=None:
            print ("{}\n".format(aux.getAgente()))
            aux=aux.getSiguiente()
    
    def toJSON(self):
        aux=self.__comienzo
        listanormal=[]
        while aux!=None:
            listanormal.append(aux.getAgente())
            aux=aux.getSiguiente()
        d=dict(
            __class__="Lista",
            agentes=[agente.toJSON() for agente in listanormal]
        )
        return d