class Persona:
    def __init__(self,nom,dir,dni):
        self.__nom=nom
        self.__dir=dir
        self.__dni=dni
    
    def get_dni(self):
        return self.__dni
    
    def __str__(self):
        return "Nombre: {}, Dirección: {}, DNI: {}".format(self.__nom,self.__dir,self.__dni)
    
    def __ne__(self,dni):
        return self.__dni!=dni