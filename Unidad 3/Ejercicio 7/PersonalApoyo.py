from Personal import Personal
class PersonalApoyo(Personal):
    def __init__(self, cuil, ape, nom, sueldo, ant, categoria):
        super().__init__(cuil, ape, nom, sueldo, ant)
        self.__categoria=categoria
    
    def __str__(self):
        print(super().__str__())
        return "Categoría: {}".format(self.__categoria)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self._Personal__cuil,
                ape=self._Personal__ape,
                nom=self._Personal__nom,
                sueldo=self._Personal__sueldo,
                ant=self._Personal__ant,
                categoria=self.__categoria
            )
        )
        return d