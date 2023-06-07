from Nodo import Nodo
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
class Lista:
    __comienzo=Nodo
    def __init__(self):
        self.__comienzo=None
    
    def ingresar_vehiculo_posicion(self,posicion,vehiculo):
        if posicion!=0:
            aux=self.__comienzo
            for i in range(posicion):
                anterior=aux
                aux=aux.getSiguiente()
            nuevonodo=Nodo(vehiculo)
            anterior.setSiguiente(nuevonodo)
            nuevonodo.setSiguiente(aux)
        else:
            self.agregarVehiculo(vehiculo)    
    
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
        print ("Vehiculo encontrado:")
        aux.getVehiculo().mostrar_datos()
            
    def modificar_precio(self,patente,nuevoprecio):
        aux=self.__comienzo
        while aux!=None:
            if isinstance(aux.getVehiculo(),VehiculoUsado):
                if patente.upper()==aux.getVehiculo().get_patente().upper():
                    break
            aux=aux.getSiguiente()
        if aux!=None:
            aux.getVehiculo().modificar_precio(nuevoprecio)
            print ("El precio de venta es:\n{}".format(aux.getVehiculo().importe_venta()))
        else:
            print ("No se encontró un vehículo con esa patente")
        print ("Vehiculo modificado:")
        aux.getVehiculo().mostrar_datos()
        
    def listarVehiculos(self):
        aux=self.__comienzo
        i=0
        while aux!=None:
            print ("Vehiculo en en la posicion {}: {}".format(i+1,aux.getVehiculo().get_modelo()))
            aux=aux.getSiguiente()
            i+=1
