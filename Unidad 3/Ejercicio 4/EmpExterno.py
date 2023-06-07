from Empleado import Empleado
class EmpExterno(Empleado):
    def __init__(self,dni,nom,dir,telf,tarea,fechainic,montoviat,costoobra,montovida,fechafin=None):
        super().__init__(dni,nom,dir,telf)
        self.__tarea=tarea
        self.__fechaini=fechainic
        self.__fechafin=fechafin
        self.__montoviat=montoviat
        self.__costobra=costoobra
        self.__montovida=montovida
    
    def get_fechafin(self):
        return self.__fechafin
    
    def get_tarea(self):
        return self.__tarea
    
    def get_costobra(self):
        return self.__costobra
    
    def sueldo(self):
        return self.__costobra-self.__montoviat-self.__montovida
    
    def mostrar_esenciales(self):
        print(super().__str__())
    
    def __str__(self):
        print(super().__str__())
        return ("Tarea {}, Fecha de inicio: {}, Fecha de Finalización: {}, Monto de viáticos: {}, Costo de la obra: {}, Monto de seguro de vida: {}".format(self.__tarea,self.__fechaini,self.__fechafin,self.__montoviat,self.__costobra,self.__montovida))