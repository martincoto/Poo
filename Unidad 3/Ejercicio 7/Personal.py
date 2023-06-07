from abc import ABC
class Personal(ABC):
    def __init__(self,cuil,ape,nom,sueldo,ant,carrera='',cargo='',catedra='',area='',tipoinv=''):
        self.__cuil=cuil
        self.__ape=ape
        self.__nom=nom
        self.__sueldo=sueldo
        self.__ant=ant
    
    def get_ape(self):
        return self.__ape
    
    def get_nom(self):
        return self.__nom
    
    def mostrar_nom_ap(self):
        print ("Apellido: {}, Nombre: {}".format(self.__ape,self.__nom))
    
    def mostrar_datos_sueldo(self):
        print ("Nombre: {}, Apellido: {}, Sueldo: {}\n".format(self.__nom,self.__ape,self.__sueldo))
    
    def __lt__(self,otro):
        return self.__ape<otro.get_ape()
    
    def __str__(self):
        return "Cuil: {}, Apellido y Nombre: {} {}, Sueldo básico: {}, Antigüedad: {}".format(self.__cuil,self.__ape,self.__nom,self.__sueldo,self.__ant)