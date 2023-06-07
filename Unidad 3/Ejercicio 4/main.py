from ManejaEmpleados import ManejaEmpleado
import os
def m_menu():
    print ("1: Registrar horas de un empleado")
    print ("2: Mostrar el monto de las tareas sin finalizar")
    print ("3: Mostrar Ayuda Económica")
    print ("4: Mostrar sueldos")
    print ("5: Mostrar todos los empleados")
    print ("6: Salir")
if __name__ == "__main__":
    empleados=ManejaEmpleado(0)
    empleados.cargar_empleados_planta()
    empleados.cargar_empleados_contratado()
    empleados.cargar_empleados_externos()
    opc=None
    while opc!='6':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            dni=input("Ingrese el DNI del empleado:\n")
            cantihoras=int(input("Ingrese la cantidad de horas a incrementar:\n"))
            empleados.registrar_horas(dni,cantihoras)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='2':
            empleados.total_tarea()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='3':
            empleados.ayuda_economica()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='4':
            empleados.mostrar_sueldos()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='5':
            empleados.mostrar_lista()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")