from Docente import Docente
from Investigador import Investigador
class DocenteInvestigador (Docente,Investigador):
    def __init__(self,cuil, ape, nom, sueldo, ant, carrera, cargo, catedra, area, tipoinv, catincentivo, impextra):
        super().__init__(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,area,tipoinv)
        self.__catincentivo=catincentivo
        self.__impextra=impextra
    
    def get_categoria(self):
        return self.__catincentivo
    
    def get_impextra(self):
        return self.__impextra
    
    def __str__(self):
        print(super().__str__())
        return "Categoría de incentivo: {}, Importe extra: {}".format(self.__catincentivo,self.__impextra)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self._Personal__cuil,
                ape=self._Personal__ape,
                nom=self._Personal__nom,
                sueldo=self._Personal__sueldo,
                ant=self._Personal__ant,
                carrera=self._Docente__carrera,
                cargo=self._Docente__cargo,
                catedra=self._Docente__catedra,
                area=self._Investigador__area,
                tipoinv=self._Investigador__tipoinv,
                catincentivo=self.__catincentivo,
                impextra=self.__impextra
            )
        )
        return d

    