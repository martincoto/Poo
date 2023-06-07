class TallerCap:
    def __init__(self,id,nom,vac,monto):
        self.__id=id
        self.__nom=nom
        self.__vacantes=vac
        self.__montoins=monto
    
    def get_id(self):
        return self.__id
    
    def get_nom(self):
        return self.__nom
    
    def get_monto (self):
        return self.__montoins
    
    def restar_vacante(self):
        self.__vacantes-=1
        
    def __str__(self):
        return "Id: {}, Nombre: {}, Vacantes: {}, Monto de inscripción: {}$".format(self.__id,self.__nom,self.__vacantes,self.__montoins)
    
    def __eq__(self,id):
        return self.__id==id