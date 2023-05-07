class conjunto:
    def __init__(self,):
        self.__conjunto = set()
    def agregarNumero(self):
        print ("Ingrese los elementos de la lista.Ingrese 0 para terminar")
        num=None
        while num!=0:
            num=int(input("Ingrese un elemento del conjunto "))
            if num!=0:
                self.__conjunto.add(num)
    def getConjunto(self):
        return self.__conjunto
    def mostrar(self):
        print(self.__conjunto)
    def __add__ (self,otroConjunto):
        return self.__conjunto.union(otroConjunto.getConjunto())
    def __sub__ (self,otroConjunto):
        return self.__conjunto.difference(otroConjunto.getConjunto())
    def __rsub__(self,otroConjunto):
        return self.__conjunto.difference(otroConjunto.getConjunto())
    def __eq__ (self,otroConjunto):
        return self.__conjunto == otroConjunto.getConjunto()