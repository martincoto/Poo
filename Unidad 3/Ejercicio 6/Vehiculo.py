from abc import ABC, abstractmethod
import json
class vehiculo(ABC):
    def __init__(self,modelo,puertas,color,preciobase,marca):
        self.__modelo=modelo
        self.__puertas=puertas
        self.__color=color
        self.__preciobase=preciobase
        self.__marca=marca
    
    def modificar_precio(self,precio):
        self.__preciobase=precio
        
    def importe_venta(self):
        pass
    
    def mostrar_modelo_puertas(self):
        print ("Modelo: {}, Cantidad de puertas: {}, ".format(self.__modelo,self.__puertas),end='')
    
    def __str__(self):
        return "Modelo: {}, Cantidad de puertas: {}, Color: {}, Precio base: {}".format(self.__modelo,self.__puertas,self.__color,self.__preciobase)
    
    def toJSON(self):
        pass