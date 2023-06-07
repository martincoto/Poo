from Empleado import Empleado
class EmpPlanta(Empleado):
    def __init__(self,dni,nom,dir,telf,sueldo,ant):
        super().__init__(dni,nom,dir,telf)
        self.__sueldo=sueldo
        self.__ant=ant
    
    def sueldo(self):
        return self.__sueldo+self.__sueldo*0.1*self.__ant
    
    def mostrar_esenciales(self):
        print(super().__str__())
        
    def __str__(self):
        print(super().__str__())
        return ("Sueldo: {}, Antigüedad: {}".format(self.__sueldo,self.__ant))