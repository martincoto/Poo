from abc import ABC, abstractmethod

class PosicionInvalidaException(Exception):
    pass

class Coleccion(ABC):
    
    @abstractmethod
    def insertarElemento(self, elemento, posicion):
        pass
    
    @abstractmethod
    def agregarElemento(self, elemento):
        pass
    
    @abstractmethod
    def mostrarElemento(self, posicion):
        pass
