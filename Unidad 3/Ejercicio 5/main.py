from Coleccion import MiColeccion
import os
def m_menu():
    print ("1: Insertar elemento en una posición")
    print ("2: Insertar elemento al final")
    print ("3: Mostrar un elemento")
    print ("4: Salir")
if __name__ == "__main__":
    colec=MiColeccion()
    opc=None
    while opc!='4':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            elemen=int(input("Ingrese el elemento a colocar:\n"))
            pos=int(input("Ingrese la posición donde desea ingresar el elemento:\n"))
            colec.insertarElemento(elemen,pos)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='2':
            elemen=int(input("Ingrese el elemento a colocar:\n"))
            colec.agregarElemento(elemen)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='3':
            pos=int(input("Ingrese la posición del elemento que desea mostrar:\n"))
            colec.mostrarElemento(pos)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")