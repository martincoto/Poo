from ManejadorReparaciones import *
from ManejadorClientes import *
import os

if __name__ == '__main__':
    opc = None
    manejadorC=ManejadorClientes()
    manejadorC.CargarClientes()
    manejadorR=ManejadorReparaciones()
    manejadorR.CargarReparaciones()
    
    while(opc != '0'):
        print('''--Menu--
        1) Mostrar Factura de Reparacion.
        2) Determinar estado de las Reparaciones del vehiculo
        3) Clientes con reparaciones pendientes
        4) Cliente que tienen mas de un Vehiculo en servicio.
        0) Terminar con el programa.
        ''')
        opc = input("Eliga una opción y presione enter: ")
        os.system('cls')    
        if opc == '1':
            manejadorC.facturaCliente(manejadorR)
            os.system('cls') 
        elif opc == '2':
            manejadorC.determinarRepa(manejadorR,manejadorC)
            os.system('cls')
        elif opc == '3':
            manejadorC.clientesPendientes(manejadorR)
            os.system('cls')
        elif opc == '4':
            manejadorC.clientesMasSv()
            os.system('cls')

    print("Hasta la proxima!! :D")