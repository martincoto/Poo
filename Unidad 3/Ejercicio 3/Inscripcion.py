class Inscripcion:
    def __init__(self,fecha,taller,persona,cond=False):
        self.__fechains=fecha
        self.__taller=taller
        self.__persona=persona
        self.__pago=cond
    
    def get_fecha(self):
        return self.__fechains
    
    def get_taller(self):
        return self.__taller
    
    def get_persona(self):
        return self.__persona
    
    def get_pago(self):
        return self.__pago
    
    def cambiar_pago(self):
        self.__pago=True
    
    def mostrar(self):
        print ("Fecha de inscripción: {}".format(self.__fechains))
        print ("Datos de la persona:")
        print (self.__persona)
        print ("Datos del taller:")
        print (self.__taller)
        print ("Condición del pago: ",end='')
        if self.__pago==False:
            print ("Sin pagar")
        else:
            print ("Pagado")