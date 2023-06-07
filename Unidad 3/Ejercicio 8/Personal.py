from abc import ABC
class Personal(ABC):
    def __init__(self,dni,cuil,ape,nom,sueldo,ant,porcentajecargo='',carrera='',cargo='',catedra='',area='',tipoinv=''):
        self.__dni=dni
        self.__cuil=cuil
        self.__ape=ape
        self.__nom=nom
        self.__sueldo=sueldo
        self.__ant=ant
    
    def get_dni(self):
        return self.__dni
    
    def get_ape(self):
        return self.__ape
    
    def get_nom(self):
        return self.__nom
    
    def get_sueldo(self):
        return self.__sueldo
    
    def modificar_sueldo(self,nuevosueld):
        self.__sueldo=nuevosueld
    
    def mostrar_nom_ap(self):
        print ("Apellido: {}, Nombre: {}".format(self.__ape,self.__nom))
    
    def mostrar_datos_sueldo(self):
        print ("Nombre: {}, Apellido: {}, Sueldo: {}\n".format(self.__nom,self.__ape,self.__sueldo))
    
    def __gt__(self,otro):
        return self.__ape<otro.get_ape()
    
    def __str__(self):
        return "DNI: {}, Cuil: {}, Apellido y Nombre: {} {}, Sueldo básico: {}, Antigüedad: {}".format(self.__dni,self.__cuil,self.__ape,self.__nom,self.__sueldo,self.__ant)