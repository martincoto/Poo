class Empleado:
    def __init__(self,dni,nom,dir,telf):
        self.__dni=dni
        self.__nom=nom
        self.__dir=dir
        self.__telf=telf
    
    def get_nom(self):
        return self.__nom
    
    def get_telf(self):
        return self.__telf
    
    def get_dni(self):
        return self.__dni
    
    def sueldo(self):
        pass
    
    def __str__(self):
        return "DNI: {}, Nombre y Apellido: {}, Dirección: {}, Teléfono: {}".format(self.__dni,self.__nom,self.__dir,self.__telf)