from zope.interface import implementer
from ITesorero import ITesorero
from IDirector import IDirector
from Nodo import Nodo
from PersonalApoyo import PersonalApoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
import os
@implementer(ITesorero)
@implementer(IDirector)
class ListaAgente:
    __comienzo=Nodo
    def __init__(self):
        self.__comienzo=None
        
    def agregar_agente(self,agente):
        nodo=Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    
    def gastosSueldoPorEmpleado(self,dni):
        aux=self.__comienzo
        band=True
        while aux!=None and band!=False:
            if dni==aux.getAgente().get_dni():
                band=False
            else:
                aux=aux.getSiguiente()
        if aux!=None:
            print("Los gastos de sueldo con el DNI {}, es de: {}$".format(dni,aux.getAgente().get_sueldo()))
        else:
            print("No se encontró a ningún agente con el DNI buscado")
    
    def modificarBasico(self,dni,nuevoBasico):
        aux=self.__comienzo
        band=True
        while aux!=None and band!=False:
            if dni==aux.getAgente().get_dni():
                band=False
            else:
                aux=aux.getSiguiente()
        if aux!=None:
            aux.getAgente().modificar_sueldo(nuevoBasico)
            print ("Se ha modificado correctamente el sueldo básico")
        else:
            print ("No se encontró ningún agente con ese DNI")
    
    def modificarPorcentajeporcargo(self,dni,nuevoPorcentaje):
        aux=self.__comienzo
        band=True
        while aux!=None and band!=False:
            if dni==aux.getAgente().get_dni():
                band=False
            else:
                aux=aux.getSiguiente()
        if aux!=None:
            if isinstance(aux.getAgente(),Docente):
                aux.getAgente().modificar_porcentajecargo(nuevoPorcentaje)
                print ("Se ha modificado correctamente el porcentaje por cargo")
            else:
                print ("El agente con el DNI ingresado, no es un Docente")
        else:
            print ("No se encontró ningún agente con ese DNI")
        
    def modificarPorcentajeporcategoria(self,dni,nuevoPorcentaje):
        aux=self.__comienzo
        band=True
        while aux!=None and band!=False:
            if dni==aux.getAgente().get_dni():
                band=False
            else:
                aux=aux.getSiguiente()
        if aux!=None:
            if isinstance(aux.getAgente(),PersonalApoyo):
                aux.getAgente().modificar_porcentajecategoria(nuevoPorcentaje)
                print ("Se ha modificado correctamente el porcentaje por cargo")
            else:
                print ("El agente con el DNI ingresado, no es un Personal de Apoyo")
        else:
            print ("No se encontró ningún agente con ese DNI")
    
    def modificarImporteExtra(self,dni,nuevoImporteExtra):
        aux=self.__comienzo
        band=True
        while aux!=None and band!=False:
            if dni==aux.getAgente().get_dni():
                band=False
            else:
                aux=aux.getSiguiente()
        if aux!=None:
            if isinstance(aux.getAgente(),DocenteInvestigador):
                aux.getAgente().modificar_importextra(nuevoImporteExtra)
                print ("Se ha modificado correctamente el porcentaje por cargo")
            else:
                print ("El agente con el DNI ingresado, no es un Docente-Investigador")
        else:
            print ("No se encontró ningún agente con ese DNI")