class Sabor:
    def __init__(self,id,ing,nom):
        self.__id=id
        self.__ingre=ing
        self.__nom=nom
        self.__cantipedidos=0
    
    def get_nom(self):
        return self.__nom
    
    def get_id(self):
        return self.__id
    
    def sumar_pedido(self):
        self.__cantipedidos+=1
    
    def get_pedidos(self):
        return self.__cantipedidos
    
    def __gt__(self,otro):
        return self.__cantipedidos<otro.get_pedidos()
        
    def mostrar(self):
        print ("Nombre:{}\nID: {}\nIngredientes: {}\nVeces pedido: {}".format(self.__nom,self.__id,self.__ingre,self.__cantipedidos))