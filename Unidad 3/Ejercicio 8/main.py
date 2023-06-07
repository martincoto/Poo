from ListaAgentes import ListaAgente
from ObjectEncoder import ObjectEncoder
from PersonalApoyo import PersonalApoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from ITesorero import ITesorero
from IDirector import IDirector
import os
def m_menu():
    print ("1: Iniciar sesión")
    print ("2: Salir")

def Tesorero(manejarTesorero:ITesorero):
        os.system('cls')
        dni=input("Ingrese el DNI del agente:\n")
        manejarTesorero.gastosSueldoPorEmpleado(dni)

def Director(manejarDirector:IDirector):
        opc=None
        while opc!=5:
            os.system('cls')
            print ("1- Modificar sueldo básico de un agente")
            print ("2- Modificar porcentaje de cargo de un Docente")
            print ("3- Modificar porcentaje de categoría de un Personal de Apoyo")
            print ("4- Modificar importe extra de un Docente-Investigador")
            print ("5- Salir")
            opc=int(input("Ingrese la opción elegida:\n"))
            os.system('cls')
            if opc==1:
                dni=input("Ingrese el DNI del agente:\n")
                sueldo=int(input("Ingrese el nuevo sueldo:\n"))
                manejarDirector.modificarBasico(dni,sueldo)
                aux=input("\nIngrese cualquier tecla para continuar\n") 
            elif opc==2:    
                dni=input("Ingrese el DNI del agente:\n")
                porc=int(input("Ingrese el porcentaje por cargo nuevo:\n"))
                manejarDirector.modificarPorcentajeporcargo(dni,porc)
                aux=input("\nIngrese cualquier tecla para continuar\n") 
            elif opc==3:
                dni=input("Ingrese el DNI del agente:\n")
                porc=int(input("Ingrese el porcentaje por categoría nuevo:\n"))
                manejarDirector.modificarPorcentajeporcategoria(dni,porc)
                aux=input("\nIngrese cualquier tecla para continuar\n") 
            elif opc==4:
                dni=input("Ingrese el DNI del agente:\n")
                imp=int(input("Ingrese el importe extra nuevo:\n"))
                manejarDirector.modificarImporteExtra(dni,imp)
                aux=input("\nIngrese cualquier tecla para continuar\n") 
if __name__ == "__main__":
    AJson=ObjectEncoder()
    agentes=ListaAgente()
    diccionario=AJson.leerJSONArchivo('personal.json')
    agentes=AJson.decodificarDiccionario(diccionario)
    opc=None
    while opc!='2':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            usuario=input("Usuario (uTesorero/uDirector):\n")
            clave=input("Clave:\n")
            if usuario.upper()=='uTesorero'.upper() and clave=='ag@74ck':
                print ("Consultar gastos de sueldo para un agente")
                Tesorero(ITesorero(agentes))
            elif usuario.upper()=='uDirector'.upper() and clave=='ufC77#!1':
                Director(ITesorero(agentes))
            aux=input("\nIngrese cualquier tecla para continuar\n")
    print("Gracias por usar el sistema")