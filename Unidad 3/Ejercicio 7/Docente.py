from Personal import Personal
class Docente(Personal):
    def __init__(self, cuil, ape, nom, sueldo, ant, carrera, cargo, catedra, area, tipoinv):
        super().__init__(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,area,tipoinv)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    
    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        print(super().__str__())
        return "Carrera: {}, Cargo: {}, Catedra: {}".format(self.__carrera,self.__cargo,self.__catedra)

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self._Personal__cuil,
                ape=self._Personal__ape,
                nom=self._Personal__nom,
                sueldo=self._Personal__sueldo,
                ant=self._Personal__ant,
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra,
                area='',
                tipoinv=''
            )
        )
        return d
    
    