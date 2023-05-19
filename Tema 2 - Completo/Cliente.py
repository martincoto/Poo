class Cliente():
    def __init__(self,dni,apell,nom,tel,paten,vehiculo,estado):
        self.__dni=dni
        self.__apellido=apell
        self.__nombre=nom
        self.__telefono=tel
        self.__patente=paten
        self.__vehiculo=vehiculo
        self.__estado=estado
    
    def getDni(self):
        return self.__dni
    def getPatente(self):
        return self.__patente
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getNomyApe(self):
        return self.__nombre+self.__apellido
    def getTelf(self):
        return self.__telefono
    def getVehiculo(self):
        return self.__vehiculo
    def getEstado(self):
        return self.__estado
    def mostrarDatosCliente(self):
        print("DNI:{:<45} Apellido y nombre:{} {}".format(self.__dni,self.__apellido,self.__nombre))
        print("Patente:{:<41} Vehiculo:{}".format(self.__patente,self.__vehiculo))
    def cambiarEstado(self,x):
        self.__estado=x
        
    def __eq__(self,Clienteb):
        Bandera=False
        #print(Clienteb.getNombre)
        #print(self.__nombre)
        if((self.__nombre)==(Clienteb.__nombre)):
            
            if((self.__dni)==(Clienteb.__dni)):
            #    print("ayuda2")
                if((self.__apellido)==(Clienteb.__apellido)):
             #       print("ayuda3")
                    if((self.__telefono)==(Clienteb.__telefono)):
              #          print("ayuda4")
                        Bandera=True

        return Bandera
        

