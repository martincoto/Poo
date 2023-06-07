from Vehiculo import vehiculo
from datetime import datetime
class VehiculoUsado(vehiculo):
    def __init__(self, modelo, puertas, color, preciobase,patente,anio,kilometraje,marca):
        super().__init__(modelo, puertas, color, preciobase,marca)
        self.__patente=patente
        self.__anio=anio
        self.__metraje=kilometraje
    
    def get_patente(self):
        return self.__patente

    def importe_venta(self):
        fecha=datetime.now()
        anio_actual=fecha.year
        if self.__metraje>100000:
            importe=self._vehiculo__preciobase-self._vehiculo__preciobase*(0.01*(anio_actual-self.__anio))-self._vehiculo__preciobase*0.02
        else:
            importe=self._vehiculo__preciobase-self._vehiculo__preciobase*(0.01*(anio_actual-self.__anio))
        return importe
    
    def mostrar_datos(self):
        print ("Vehículo Usado:")
        print (super().__str__())
        print ("Patente: {}, Año: {}, Kilometraje: {}".format(self.__patente,self.__anio,self.__metraje))
    