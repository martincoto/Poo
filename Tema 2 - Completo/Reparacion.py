class Reparacion():
    __rprecio=float
    __manoprecio=float
    def __init__(self,patent,repa,rp,pm,estado):
        self.__patente=patent
        self.__reparacion=repa
        self.__rprecio=rp
        self.__manoprecio=pm
        self.__estado=estado

    def getPatentex(self):
        return self.__patente
    def getReparacion(self):
        return self.__reparacion
    def getRPrecio(self):
        return self.__rprecio
    def getManoPrecio(self):
        return self.__manoprecio
    def getEstado(self):
        return self.__estado