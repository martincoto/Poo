class Nodo:
    def __init__(self,vehiculo):
        self.__vehiculo=vehiculo
        self.__siguiente=None
    
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getVehiculo(self):
        return self.__vehiculo