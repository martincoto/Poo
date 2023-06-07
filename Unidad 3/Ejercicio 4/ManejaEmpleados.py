import numpy as np
import Empleado
from EmpPlanta import EmpPlanta
from EmpContratado import EmpContratado
from EmpExterno import EmpExterno
import csv
class ManejaEmpleado:
    def __init__(self,dimension,incremento=5):
        self.__listaemp=np.empty(dimension,dtype=object)
        self.__cantidad=0
        self.__incremento=incremento
        self.__dimension=dimension
        
    def cargar_empleados_planta(self):
        archivo=open ("planta.csv",encoding='utf8')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            plantaaux=EmpPlanta(fila[0],fila[1],fila[2],fila[3],float(fila[4]),int(fila[5]))
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__listaemp.resize(self.__dimension)
            self.__listaemp[self.__cantidad]=plantaaux
            self.__cantidad+=1
    
    def cargar_empleados_contratado(self):
        archivo=open ("contratados.csv",encoding='utf8')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            contratadosaux=EmpContratado(fila[0],fila[1],fila[2],fila[3],fila[4],int(fila[6]),float(fila[7]),fila[5])
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__listaemp.resize(self.__dimension)
            self.__listaemp[self.__cantidad]=contratadosaux
            self.__cantidad+=1
    
    def cargar_empleados_externos(self):
        archivo=open ("externos.csv",encoding='utf8')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            externoaux=EmpExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],float(fila[7]),float(fila[8]),float(fila[9]),fila[6])
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__listaemp.resize(self.__dimension)
            self.__listaemp[self.__cantidad]=externoaux
            self.__cantidad+=1
            
    def mostrar_lista (self):
        for empleado in self.__listaemp:
            print (empleado)
            print("\n")
    
    def registrar_horas(self,dni,cantihoras):
        i=0
        band=False
        while i<len(self.__listaemp) and band==False:
            if isinstance(self.__listaemp[i],EmpContratado):
                if dni==self.__listaemp[i].get_dni():
                    band=True
            i+=1
        if i<len(self.__listaemp):
            self.__listaemp[i].modificar_cantihoras(cantihoras)
            print ("Se han incrementado las horas del empleado correctamente")
        else:
            print ("No se ha encontrado a la persona buscada")
    
    def total_tarea(self):
        print ("El monto a pagar por las tareas sin finalizar son")
        for empleado in self.__listaemp:
            if isinstance(empleado,EmpExterno):
                if empleado.get_fechafin()=='Sin Finalizar' or None:
                    print ("El costo de la tarea {} es:\n {}$".format(empleado.get_tarea(),empleado.get_costobra()))
            
    def ayuda_economica(self):
        print ("Los empleados que se les otorgará ayuda económica son:")
        for empleado in self.__listaemp:
            if empleado.sueldo()<150000:
                empleado.mostrar_esenciales()
    
    def mostrar_sueldos(self):
        print ("Los sueldos de los empleados son:")
        for empleado in self.__listaemp:
            print ("Nombre: {:<20} Teléfono: {:<10} Sueldo: {:<9}$".format(empleado.get_nom(),empleado.get_telf(),str(empleado.sueldo())))