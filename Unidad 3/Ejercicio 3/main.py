from ManejaTalleres import ManejaTaller
from ManejaPersonas import ManejaPersona
from ManejaInscripcion import ManejaInscripcion
import os
def m_menu():
    print ("1: Registrar inscripción")
    print ("2: Mostrar taller y monto que adeuda una persona")
    print ("3: Listar inscriptos de un taller")
    print ("4: Registrar pago de una persona")
    print ("5: Generar archivo nuevo con datos de las inscripciones")
    print ("6: Mostrar Talleres, Inscriptos, y Personas")
    print ("7: Salir")
if __name__ == "__main__":
    talleres=ManejaTaller()
    personas=ManejaPersona()
    inscripciones=ManejaInscripcion()
    talleres.cargar_talleres()
    opc=None
    while opc!='7':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            personaaux=inscripciones.cargar_inscripciones(talleres)
            personas.cargar_persona(personaaux)
        if opc=='2':
            dni=input("Ingrese el DNI de la persona a buscar:\n")
            inscripciones.buscar_inscripto(dni)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='3':
            id=input("Ingrese la ID del taller a mostrar los inscriptos:\n")
            print ("Los inscriptos al taller {} son:".format(id))
            inscripciones.mostrar_inscriptos_taller(id)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='4':
            dni=input("Ingrese el DNI de la persona a buscar:\n")
            inscripciones.cambiar_pago_persona(dni)
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='5':
            inscripciones.generar_archivo()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
        if opc=='6':
            print ("Talleres:")
            talleres.mostrar_talleres()
            print ("Personas:")
            personas.mostrar_personas()
            print ("Inscripciones:")
            inscripciones.mostrar()
            aux=input("\nIngrese cualquier tecla para continuar\n") 
    print("Gracias por usar el sistema")