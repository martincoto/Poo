from Personal import Personal
class Investigador(Personal):
    def __init__(self, cuil, ape, nom, sueldo, ant, carrera, cargo, catedra, area, tipoinv):
        super().__init__(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,area,tipoinv)
        self.__area=area
        self.__tipoinv=tipoinv

    def get_area(self):
        return self.__area
    
    def __str__(self):
        print(super().__str__())
        return "Area: {}, Tipo de Investigación: {}".format(self.__area,self.__tipoinv)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self._Personal__cuil,
                ape=self._Personal__ape,
                nom=self._Personal__nom,
                sueldo=self._Personal__sueldo,
                ant=self._Personal__ant,
                area=self.__area,
                tipoinv=self.__tipoinv,
                carrera='',
                cargo='',
                catedra=''
            )
        )
        return d
    
    