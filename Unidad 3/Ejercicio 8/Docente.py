from Personal import Personal
class Docente(Personal):
    def __init__(self, dni, cuil, ape, nom, sueldo, ant, porcentajecargo, carrera, cargo, catedra, area, tipoinv):
        super().__init__(dni,cuil,ape,nom,sueldo,ant,porcentajecargo,carrera,cargo,catedra,area,tipoinv)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__porcentajecargo=porcentajecargo
        self.__catedra=catedra
    
    def get_carrera(self):
        return self.__carrera

    def modificar_porcentajecargo(self,nuevoporc):
        self.__porcentajecargo=nuevoporc
    
    def __str__(self):
        print(super().__str__())
        return "Carrera: {}, Cargo: {}, Porcentaje de cargo: {}%, Catedra: {}".format(self.__carrera,self.__cargo, self.__porcentajecargo,self.__catedra)

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                dni=self._Personal__dni,
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