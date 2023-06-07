from Inscripcion import Inscripcion
from Persona import Persona
import csv
class ManejaInscripcion:
    def __init__(self):
        self.__listainsc=[]
        
    def cargar_inscripciones(self,listatalleres):
        print ()
        nomtaller=input("Ingrese el nombre del taller a inscribir\n")
        taller=listatalleres.buscar_taller(nomtaller)
        if taller==False:
            print ("No se encontró el taller a buscar")
        else:
            nom=input("Ingrese el nombre y apellido:\n")
            dir=input("Ingrese la dirección de la persona:\n")
            dni=input("Ingrese el DNI de la persona:\n")
            persona=Persona(nom,dir,dni)
            fecha=input("Ingrese la fecha de la inscripción (DD/MM/AA):\n")
            inscripcionaux=Inscripcion(fecha,taller,persona)
            self.__listainsc.append(inscripcionaux)
            return persona
    
    def mostrar (self):
        for inscripcion in self.__listainsc:
            inscripcion.mostrar()
    
    def cambiar_pago_persona(self,dni):
        i=0
        while i<len(self.__listainsc) and self.__listainsc[i].get_persona()!=dni:
            i+=1
        if i<len(self.__listainsc):
            if self.__listainsc[i].get_pago()==False:
                self.__listainsc[i].cambiar_pago()
                print ("Se ha registrado el pago")
            else:
                print ("No debe nada")
        else:
            print ("No se encontró a la persona buscada")
            
    def buscar_inscripto (self,dni):
        i=0
        while i<len(self.__listainsc) and self.__listainsc[i].get_persona()!=dni:
            i+=1
        if i<len(self.__listainsc):
            print ("Datos del taller del DNI ingresado:")
            print(self.__listainsc[i].get_taller())
            if self.__listainsc[i].get_pago()==False:
                print ("El monto que adeuda es: {}$".format(self.__listainsc[i].get_taller().get_monto()))
            else:
                print ("No debe nada")
        else:
            print ("No se encontró a la persona buscada")
    
    def mostrar_inscriptos_taller(self,id):
        for inscripto in self.__listainsc:
            if inscripto.get_taller()==id:
                print (inscripto.get_persona())
                
    def generar_archivo(self):
        archivo="Inscriptos.csv"
        with open(archivo,'w',newline='') as archivo_csv:
            writer=csv.writer(archivo_csv,delimiter=';')
            for inscripto in self.__listainsc:
                fila=[inscripto.get_persona().get_dni(),inscripto.get_taller().get_id(),inscripto.get_fecha(),inscripto.get_pago()]
                writer.writerow(fila)
        print ("Se ha cargado correctamente")
