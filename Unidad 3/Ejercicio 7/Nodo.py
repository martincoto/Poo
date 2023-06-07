class Nodo:
    def __init__(self,agente):
        self.__agente=agente
        self.__siguiente=None
    
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getAgente(self):
        return self.__agente