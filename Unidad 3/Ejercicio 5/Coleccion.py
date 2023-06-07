from Interface import *
class MiColeccion(Coleccion):
    
    def __init__(self):
        self.elementos = []
    
    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > len(self.elementos):
            raise PosicionInvalidaException("La posición de inserción no es válida.")
        self.elementos.insert(posicion, elemento)
    
    def agregarElemento(self, elemento):
        self.elementos.append(elemento)
    
    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.elementos):
            raise PosicionInvalidaException("La posición no es válida.")
        return self.elementos[posicion]
