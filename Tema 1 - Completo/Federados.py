class Federados():
    __apellido=''
    __nombre=''
    __dni=''
    __edad=''
    __club=''
    
    def __init__(self,ape,nom,dni,edad,club):
        self.__apellido=ape
        self.__nombre=nom
        self.__dni=dni
        self.__edad=edad
        self.__club=club

    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getEdad(self):
        return self.__edad
    def getClub(self):
        return self.__club
    
    def mostrarDatos(self):
        print("{} {} {} {} {}".format(self.__apellido,self.__nombre,self.__dni,self.__edad,self.__club))
    
    def mostrarDatos1(self):
        print("{:<12} {:<12} {:<12}".format(self.__apellido,self.__nombre,self.__dni))
    
    def mostrarDatos2(self,estilo):
        print("{:<12} {:<12} {:<12} {:<12}".format(self.__apellido,self.__nombre,estilo,self.__club))
    
    