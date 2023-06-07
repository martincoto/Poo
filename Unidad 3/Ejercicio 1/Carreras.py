class Carrera:
    def __init__(self,cod,nom,fechain,dur,titu):
        self.__cod=cod
        self.__nom=nom
        self.__fecha=fechain
        self.__dur=dur
        self.__titulo=titu

    def get_cod(self):
        return self.__cod
    
    def get_nom(self):
        return self.__nom
    
    def mostrar_car(self):
        print ("    {} - {}, {}, {}, {},".format(self.__cod,self.__nom,self.__fecha,self.__dur,self.__titulo))

    def mostrar_dur(self):
        print ("Carrera: {}".format(self.__nom))
        print ("Duración: {}".format(self.__dur))