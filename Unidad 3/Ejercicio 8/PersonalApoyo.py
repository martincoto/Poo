from Personal import Personal
class PersonalApoyo(Personal):
    def __init__(self, dni, cuil, ape, nom, sueldo, ant, categoria, porcentajecategoria):
        super().__init__(dni, cuil, ape, nom, sueldo, ant)
        self.__categoria=categoria
        self.__porcentajecategoria=porcentajecategoria
    
    def modificar_porcentajecategoria(self,nuevoporc):
        self.__porcentajecategoria=nuevoporc
    
    def __str__(self):
        print(super().__str__())
        return "Categoría: {}, Porcentaje por Categoría: {}%".format(self.__categoria,self.__porcentajecategoria)
    
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
                categoria=self.__categoria
            )
        )
        return d