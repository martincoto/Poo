from ManejaSabores import ManejaSabor
from ManejaHelados import ManejaHelado

import os
def m_menu():
    print ("1: Registrar helado vendido")
    print ("2: Mostrar los 5 helados más pedidos")
    print ("3: Total de gramos vendidos de un sabor")
    print ("4: Mostrar los sabores vendidos por un tipo de helado")
    print ("5: Total recaudado por tipo de helado")
    print ("6: Mostrar helados")
    print ("7: Salir")
if __name__ == "__main__":
    sabores=ManejaSabor()
    sabores.cargar_sabores()
    helados=ManejaHelado()
    opc=None
    while opc!='7':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            helados.cargar_helado(sabores)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='2':
            sabores.mostrar_mas_pedidos()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='3':
            id=input("Ingrese la ID del helado a buscar:\n")
            helados.estimar_gramos(id)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='4':
            print("1- 100gr")
            print("2- 150gr")
            print("3- 250gr")
            print("4- 500gr")
            print("5- 1000gr")
            tipohelado=input("Ingrese el tipo de helado:\n")
            helados.mostrar_por_tipohelados(tipohelado)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='5':
            helados.calcular_total()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='6':
            helados.mostrar_helados()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")