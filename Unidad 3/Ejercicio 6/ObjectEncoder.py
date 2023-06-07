import json
from pathlib import Path
from Vehiculo import vehiculo
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
from ListaVehiculos import Lista
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                vehiculos=d['vehiculos']
                lista=class_()
                i=0
                for i in range(len(vehiculos)):
                    dvehiculos=vehiculos[i]
                    class_name=dvehiculos.pop('__class__')
                    class_=eval(class_name)
                    atributos=dvehiculos['__atributos__']
                    unVehiculo=class_(**atributos)
                    #unVehiculo.mostrar_datos()
                    lista.agregarVehiculo(unVehiculo)
            return lista
            
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:json.dump(diccionario, destino, indent=4)
        destino.close()
        
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:diccionario=json.load(fuente)
        fuente.close()
        return diccionario
    
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)