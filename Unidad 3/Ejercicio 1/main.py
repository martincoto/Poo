from ManejaFacultades import ManejaFacultad
import os
def m_menu():
    print ("1: Mostrar facultades")
    print ("2: Mostrar facultad con carreras")
    print ("3: Mostrar datos de una carrera")
    print ("4: Salir")
    
if __name__=='__main__':
    fac=ManejaFacultad()
    fac.cargar_archivo()
    opc=None
    while opc!='4':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            fac.mostrar_facultades()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='2':
            cod=int(input("Ingrese el código de carrera a buscar:\n"))
            os.system('cls')
            ind=fac.buscar_facultad(cod)
            fac.mostrar_facultad_carreras(ind)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='3':
            nom=input("Ingrese el nombre de la carrera:\n")
            fac.buscar_carrera(nom)  
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")