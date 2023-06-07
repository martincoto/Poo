from ObjectEncoder import ObjectEncoder
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
from ListaVehiculos import Lista
import os
def m_menu():
    print ("1: Ingresar un vehículo en una posición")
    print ("2: Agregar un vehículo a la colección")
    print ("3: Mostrar tipo de objeto de una posición de la lista")
    print ("4: Modificar precio base, y mostrar nuevo precio de venta")
    print ("5: Mostrar todos los datos del vehículo más económico")
    print ("6: Mostrar modelo, cantidad de puertas e importe de venta, de todos los vehículos")
    print ("7: Almacenar en un archivo los autos")
    print ("8: Salir")
if __name__ == "__main__":
    jsonV=ObjectEncoder()
    vehiculos=Lista()
    diccionario=jsonV.leerJSONArchivo('vehiculos.json')
    vehiculos=jsonV.decodificarDiccionario(diccionario)
    opc=None
    while opc!='8':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            print ("Ingrese el vehículo")
            tipoveh= int(input("1 - Nuevo\n2 - Usado\n"))
            if tipoveh==1:
                mod=input("Ingrese el modelo:\n")
                cantipuer=input("Ingrese la cantidad de puertas:\n")
                color=input("Ingrese el color:\n")
                preciobase=int(input("Ingrese el precio base:\n"))
                version=input("Ingrese la versión:\n")
                marca=input("Ingrese la marca:\n")
                vehiculoaux=VehiculoNuevo(mod,cantipuer,color,preciobase,version,marca)
            elif tipoveh==2:
                mod=input("Ingrese el modelo:\n")
                cantipuer=input("Ingrese la cantidad de puertas:\n")
                color=input("Ingrese el color:\n")
                preciobase=int(input("Ingrese el precio base:\n"))
                patente=input("Ingrese la patente:\n")
                anio=int(input("Ingrese el año:\n"))
                metraje=int(input("Ingrese el kilometraje:\n"))
                marca=input("Ingrese la marca:\n")
                vehiculoaux=VehiculoUsado(mod,cantipuer,color,preciobase,patente,anio,metraje,marca)
            posicion=int(input("Ingrese la posición donde quiere ingresar el vehículo:\n"))-1
            vehiculos.ingresar_vehiculo_posicion(posicion,vehiculoaux)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='2':
            print ("Ingrese el vehículo")
            tipoveh= int(input("1 - Nuevo\n2 - Usado\n"))
            if tipoveh==1:
                mod=input("Ingrese el modelo:\n")
                cantipuer=input("Ingrese la cantidad de puertas:\n")
                color=input("Ingrese el color:\n")
                preciobase=int(input("Ingrese el precio base:\n"))
                version=input("Ingrese la versión:\n")
                marca=input("Ingrese la marca:\n")
                vehiculoaux=VehiculoNuevo(mod,cantipuer,color,preciobase,version,marca)
            elif tipoveh==2:
                mod=input("Ingrese el modelo:\n")
                cantipuer=input("Ingrese la cantidad de puertas:\n")
                color=input("Ingrese el color:\n")
                preciobase=int(input("Ingrese el precio base:\n"))
                patente=input("Ingrese la patente:\n")
                anio=int(input("Ingrese el año:\n"))
                metraje=int(input("Ingrese el kilometraje:\n"))
                marca=input("Ingrese la marca:\n")
                vehiculoaux=VehiculoUsado(mod,cantipuer,color,preciobase,patente,anio,metraje,marca)
            vehiculos.agregarVehiculo(vehiculoaux)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='3':
            posicion=int(input("Ingrese la posición del vehículo:\n"))-1
            vehiculos.mostrar_tipo_vehiculo(posicion)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='4':
            patente=input("Ingrese la Patente del vehículo:\n")
            vehiculos.modificar_precio(patente)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='5':
            vehiculos.mostrar_economico()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='6':
            vehiculos.listarVehiculos()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='7':
            d=vehiculos.toJSON()
            jsonV.guardarJSONArchivo(d,'vehiculosnuevos.json')
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")