from Empleado import Empleado
class EmpContratado(Empleado):
    def __init__(self,dni,nom,dir,telf,fechainic,cantihoras,valorhora,fechafin=None):
        super().__init__(dni,nom,dir,telf)
        self.__fechaini=fechainic
        self.__canthoras=cantihoras
        self.__valorhora=valorhora
        self.__fechafin=fechafin
    
    def get_cantihoras(self):
        return self.__canthoras
    
    def modificar_cantihoras(self,cantihoras):
        self.__canthoras+=cantihoras
    
    def sueldo(self):
        return self.__canthoras*self.__valorhora

    def mostrar_esenciales(self):
        print(super().__str__())
        
    def __str__(self):
        print(super().__str__())
        return ("Fecha de inicio: {}, Fecha de Finalización: {}, Cantidad de horas: {}, Valor por hora: {}".format(self.__fechaini,self.__fechafin,self.__canthoras,self.__valorhora))