class Facultad:
    def __init__(self, cod, nom, dir, loc, telf, carrera=None):
        self.__cod = cod
        self.__nom = nom
        self.__dir = dir
        self.__loc = loc
        self.__telf = telf
        self.__listacarreras = []
        if (carrera != None):
            self.__listacarreras.append(carrera)

    def get_cod(self):
        return self.__cod
    
    def get_loc(self):
        return self.__loc
    
    def get_nom(self):
        return self.__nom
    
    def mostrar_fac(self):
        print ("{} - {}, {}, {}, {}".format(self.__cod,self.__nom,self.__dir,self.__loc,self.__telf))

    def mostrar(self):
        print ("{} - {}, {}, {}, {}".format(self.__cod,self.__nom,self.__dir,self.__loc,self.__telf))
        for carrera in self.__listacarreras:
            carrera.mostrar_car()

    def mostrar_car_dur(self):
        print ("Nombre de Facultad: {}".format(self.__nom))
        for carrera in self.__listacarreras:
            carrera.mostrar_dur()
    def agregar_carrera(self,carrera):
        self.__listacarreras.append(carrera)
        
    def buscar_carreras(self,nom):
        i=0
        while i<len(self.__listacarreras) and nom.upper()!=self.__listacarreras[i].get_nom().upper():
            i+=1
        if i<len(self.__listacarreras):
            print ("Datos de la carrera ingresada:")
            print ("Nombre: "+self.__listacarreras[i].get_nom())
            print ("Código de carrera: "+str(self.__listacarreras[i].get_cod()))
            i=True
        else:
            i=False
        return i