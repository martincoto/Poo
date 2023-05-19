
import csv
from Cliente import *
from ManejadorReparaciones import *

class ManejadorClientes():
    __listac=[]
    def __init__(self):
        __listac=[]

    def CargarClientes(self):
        archivo=open('clientes.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltearFila=True 
        for fila in reader:
            if saltearFila:
                saltearFila=False
            else:
                unCliente=Cliente(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__listac.append(unCliente)
    
    def facturaCliente(self,manejadorR):
        dni=input("Ingrese el dni del cliente: ")
        i=0
        j=0
        total=0
        
        while i<(len(self.__listac)):
            if dni==(self.__listac[i].getDni()):
                self.__listac[i].mostrarDatosCliente()
                listar=manejadorR.getListaR()
                print("{:<30}{:<20}{:<17}Subtotal".format("Reparación","Precio Repuesto","Mano de Obra"))
                while j<(len(listar)):
                    if (self.__listac[i].getPatente()==listar[j].getPatentex()):
                       
                        manejadorR.mostrarDatosReparacion(j)
                        total=total+manejadorR.subtotal(j)
                    j+=1
                print("                                               Totala a pagar:     ${:.2f}".format(total))
            i+=1
        input("\n--------Presione enter para volver al menu---------")
    
    
    
    def determinarRepa(self,manejadorR,manejadorC):
        patente=input("Ingresa la patente de un vehiculo: ")
        i=0
        j=0
        total=0
        listar=manejadorR.getListaR()
        #print(len(listar))
        while i<len(listar):
            #print(i)
            if (patente==listar[i].getPatentex()):
                if(listar[i].getEstado()=='T'):
                    j=manejadorC.buscarPatente(patente)
                    self.__listac[j].cambiarEstado('T')
                    total=total+manejadorR.subtotal(i)                         
                else:
                    print("La reparacion todavia esta pendiente")
            i=i+1
        print(''' Nombre y apellido: {}\n telefono: {}\n vehiculo: {}\n estado: {}'''.format(self.__listac[j].getNomyApe(),self.__listac[j].getTelf(),
                                                          self.__listac[j].getVehiculo(),self.__listac[j].getEstado()))
        print("Total a pagar: ",total)    
        input("\n--------Presione enter para volver al menu---------")
    
    def buscarPatente(self,patente):
        j=0
        while(j<len(self.__listac)):
            if(patente==self.__listac[j].getPatente()):
                return j
            j=j+1
    
    def clientesPendientes(self,manejadorR):
        i=0
        j=0
        while i<(len(self.__listac)):
           
            if(self.__listac[i].getEstado()=='P'):
                print("-------------------------------------------------------------------------------------------------")
                print("Apellido y Nombre: {:<30} Telefono: {}".format(self.__listac[i].getNomyApe(),self.__listac[i].getTelf()))
                print("Patente:{:<45}Vehiculo:{}".format(self.__listac[i].getPatente(),self.__listac[i].getVehiculo()))
                listar=manejadorR.getListaR()
                print("Reparacion")
                while j<len(listar):
                    #print(self.__listac[i].getPatente())
                    #print(listar[j].getPatentex())
                    if ((self.__listac[i].getPatente())==(listar[j].getPatentex())):
                        #print(j)
                        print(listar[j].getReparacion())
                    j=j+1
                j=0
            i=i+1
        input("\n---------------------Presione enter para volver al menu----------------------------------------")
    def clientesMasSv(self):
        i=0
        while i<len(self.__listac):
            j=i+1
            while j<len(self.__listac):
                #print(self.__listac[i].__eq__(self.__listac[j]))
                if (self.__listac[i].__eq__(self.__listac[j])):
                    print("-------------------------------------------------------------------------------------------------")
                    print("Dni: ",self.__listac[i].getDni())
                    print("Apellido y Nombre: {:<30} Telefono: {}".format(self.__listac[i].getNomyApe(),self.__listac[i].getTelf()))
                    print("Patente:{:<45}Vehiculo:{}".format(self.__listac[i].getPatente(),self.__listac[i].getVehiculo()))
                j=j+1
            
            i=i+1
        input("\n----------------------Presione enter para volver al menu----------------------------------------")                
