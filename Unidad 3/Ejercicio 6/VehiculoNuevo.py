from Vehiculo import vehiculo
class VehiculoNuevo(vehiculo):
    def __init__(self, modelo, puertas, color, preciobase,version,marca):
        super().__init__(modelo, puertas, color, preciobase,marca)
        self.__version=version
        
    def importe_venta(self):
        if self.__version=='Full':
            importe=self._vehiculo__preciobase+self._vehiculo__preciobase*0.1+self._vehiculo__preciobase*0.02
        else:
            importe=self._vehiculo__preciobase+self._vehiculo__preciobase*0.1
        return importe
    
    def mostrar_datos(self):
        print ("Vehículo Nuevo:")
        print (super().__str__())
        print ("Versión: {}, Marca: {}".format(self.__version,self.__marca))
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self._vehiculo__modelo,
                puertas=self._vehiculo__puertas,
                color=self._vehiculo__color,
                preciobase=self._vehiculo__preciobase,
                version=self.__version,
                marca=self._vehiculo__marca
            )
        )
        return d