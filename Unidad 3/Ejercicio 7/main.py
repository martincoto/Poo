from ListaAgentes import ListaAgente
from ObjectEncoder import ObjectEncoder
from PersonalApoyo import PersonalApoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
import os
def m_menu():
    print ("1: Ingresar un agente en una posición")
    print ("2: Agregar un agente a la colección")
    print ("3: Mostrar tipo de objeto de una posición de la lista")
    print ("4: Generar un listado de los Docentes-Investigadores de una carrera")
    print ("5: Mostrar la cantidad de Docentes-Investigadores e Investigadores de un área")
    print ("6: Mostrar listado ordenado por apellido")
    print ("7: Mostrar Docentes-Investigadores, y total de dinero de importe extra por categoría")
    print ("8: Almacenar los datos en un archivo")
    print ("9: Salir")
if __name__ == "__main__":
    AJson=ObjectEncoder()
    agentes=ListaAgente()
    diccionario=AJson.leerJSONArchivo('personal.json')
    agentes=AJson.decodificarDiccionario(diccionario)
    agentes.mostrar_lista()
    opc=None
    while opc!='9':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            print ("Ingrese el agente")
            tipoag= int(input("1 - Personal de Apoyo\n2 - Docente\n3 - Investigador\n4 - Docente-Investigador\n"))
            if tipoag==1:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                categoria=input("Ingrese la categoría:\n")
                agenteaux=PersonalApoyo(cuil,ape,nom,sueldo,ant,categoria)
            elif tipoag==2:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                carrera=input("Ingrese la carrera:\n")
                cargo=input("Ingrese el cargo:\n")
                catedra=input("Ingrese la cátedra:\n")
                agenteaux=Docente(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,'','')
            elif tipoag==3:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                area=input("Ingrese el área:\n")
                tipoinv=input("Ingrese el tipo de investigación:\n")
                agenteaux=Investigador(cuil,ape,nom,sueldo,ant,'','','',area,tipoinv)
            elif tipoag==4:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                carrera=input("Ingrese la carrera:\n")
                cargo=input("Ingrese el cargo:\n")
                catedra=input("Ingrese la cátedra:\n")
                area=input("Ingrese el área:\n")
                tipoinv=input("Ingrese el tipo de investigación:\n")
                catincentivo=input("Ingrese la categoría de incentivo:\n")
                impextra=int(input("Ingrese el importe extra: \n"))
                agenteaux=DocenteInvestigador(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,area,tipoinv,catincentivo,impextra)
            posicion=int(input("Ingrese la posición donde quiere ingresar el agente:\n"))-1
            agentes.insertar_agente(posicion,agenteaux)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='2':
            print ("Ingrese el agente")
            tipoag= int(input("1 - Personal de Apoyo\n2 - Docente\n3 - Investigador\n4 - Docente-Investigador\n"))
            if tipoag==1:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                categoria=input("Ingrese la categoría:\n")
                agenteaux=PersonalApoyo(cuil,ape,nom,sueldo,ant,categoria)
            elif tipoag==2:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                carrera=input("Ingrese la carrera:\n")
                cargo=input("Ingrese el cargo:\n")
                catedra=input("Ingrese la cátedra:\n")
                agenteaux=Docente(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,'','')
            elif tipoag==3:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                area=input("Ingrese el área:\n")
                tipoinv=input("Ingrese el tipo de investigación:\n")
                agenteaux=Investigador(cuil,ape,nom,sueldo,ant,'','','',area,tipoinv)
            elif tipoag==4:
                cuil=int(input("Ingrese el cuil:\n"))
                ape=input("Ingrese el apellido:\n")
                nom=input("Ingrese el nombre:\n")
                sueldo=int(input("Ingrese el sueldo:\n"))
                ant=int(input("Ingrese la antigüedad:\n"))
                carrera=input("Ingrese la carrera:\n")
                cargo=input("Ingrese el cargo:\n")
                catedra=input("Ingrese la cátedra:\n")
                area=input("Ingrese el área:\n")
                tipoinv=input("Ingrese el tipo de investigación:\n")
                catincentivo=input("Ingrese la categoría de incentivo:\n")
                impextra=int(input("Ingrese el importe extra: \n"))
                agenteaux=DocenteInvestigador(cuil,ape,nom,sueldo,ant,carrera,cargo,catedra,area,tipoinv,catincentivo,impextra)
            agentes.agregar_agente(agenteaux)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='3':
            posicion=int(input("Ingrese la posición del agente:\n"))-1
            agentes.mostrar_objeto_posicion(posicion)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='4':
            carrera=input("Ingrese la carrera:\n")
            agentes.listado_carrera(carrera)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='5':
            area=input("Ingrese el área de investigación:\n")
            agentes.contar_agentes(area)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='6':
            agentes.generar_listado()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='7':
            cat=input("Ingrese la categoría:\nI / II / III / IV / V\n")
            agentes.mostrar_categoria(cat)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        elif opc=='8':
            d=agentes.toJSON()
            AJson.guardarJSONArchivo(d,'nuevopersonal.json')
            print ("Se ha guardado correctamente el personal")
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")