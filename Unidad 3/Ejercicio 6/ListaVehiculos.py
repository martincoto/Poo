from Nodo import Nodo
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
class Lista:
    __comienzo=Nodo
    def __init__(self):
        self.__comienzo=None
    
    def ingresar_vehiculo_posicion(self,posicion,vehiculo):
        aux=self.__comienzo
        for i in range(posicion):
            anterior=aux
            aux=aux.getSiguiente()
        nuevonodo=Nodo(vehiculo)
        anterior.setSiguiente(nuevonodo)
        nuevonodo.setSiguiente(aux)    
    
    def agregarVehiculo(self,vehiculo):
        nodo=Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    
    def mostrar_tipo_vehiculo(self,posicion):
        aux=self.__comienzo
        for i in range(posicion):
            aux=aux.getSiguiente()
        if isinstance(aux.getVehiculo(),VehiculoNuevo):
            print ("El vehículo en esa posición es un Vehículo Nuevo")
        elif isinstance(aux.getVehiculo(),VehiculoUsado):
            print ("El vehículo en esa posición es un Vehículo Usado")
            
    def modificar_precio(self,patente):
        aux=self.__comienzo
        while aux!=None:
            if isinstance(aux.getVehiculo(),VehiculoUsado):
                if patente.upper()==aux.getVehiculo().get_patente().upper():
                    break
            aux=aux.getSiguiente()
        if aux!=None:
            nuevoprecio=int(input("Ingrese el nuevo precio:\n"))
            aux.getVehiculo().modificar_precio(nuevoprecio)
            print ("El precio de venta es:\n{}".format(aux.getVehiculo().importe_venta()))
        else:
            print ("No se encontró un vehículo con esa patente")
    
    def mostrar_economico(self):
        aux=self.__comienzo
        vehieco=None
        precio=99999999
        while aux!=None:
            if aux.getVehiculo().importe_venta()<precio:
                precio=aux.getVehiculo().importe_venta()
                vehieco=aux.getVehiculo()
            aux=aux.getSiguiente()
        print ("El vehículo más económico es:")
        vehieco.mostrar_datos()
        print ("Importe de Venta: {}".format(vehieco.importe_venta()))
        
    def listarVehiculos(self):
        aux=self.__comienzo
        while aux!=None:
            aux.getVehiculo().mostrar_modelo_puertas()
            print ("Importe de Venta: {}".format(aux.getVehiculo().importe_venta()))
            aux=aux.getSiguiente()
    
    def toJSON(self):
        aux=self.__comienzo
        listanormal=[]
        while aux!=None:
            listanormal.append(aux.getVehiculo())
            aux=aux.getSiguiente()
        d=dict(
            __class__="Lista",
            vehiculos=[vehiculo.toJSON() for vehiculo in listanormal]
        )
        return d