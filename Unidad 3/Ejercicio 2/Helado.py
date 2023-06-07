class Helado:
    __listasab=[]
    def __init__(self,gramos,precio):
        self.__gramos=gramos
        self.__precio=precio
        self.__listasab=[]
    
    def cargar_sabores(self,listasabores,nomsab):
        saboraux=listasabores.get_sabor(nomsab)
        if (saboraux==None):
            return
        self.__listasab.append(saboraux)
    
    def get_gramo(self):
        return self.__gramos
    
    def get_precio(self):
        return self.__precio
    
    def get_gramos(self,id):
        i=0
        while i<len(self.__listasab) and id!=self.__listasab[i].get_id():
            i+=1
        if i<len(self.__listasab):
            i=self.__gramos/len(self.__listasab)
        else:
            i=0
        return i
    
    def mostrar_sabores(self):
        for sabor in self.__listasab:
            print (sabor.get_nom())
    
    def mostrar(self):
        print ("Peso: {}gr, Precio: {}$".format(self.__gramos,self.__precio))
        print ("Sabores:")
        for sabor in self.__listasab:
            print (sabor.get_nom())
