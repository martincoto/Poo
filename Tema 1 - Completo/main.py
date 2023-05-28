from manejadorEvaluaciones import *
from manejadorFederados import *
import os

if __name__ == '__main__':
    unMf=manejadorFederados()
    unMf.cargaLista()
#    unMf.mostrarLista()
    unME=manejadorEvaluaciones()
    unME.cargaListaE()
    listaE=unME.guardaLista()
    opc = None
    
    while(opc != '0'):
        print('''--Menu--
        1)Leer un estilo y una edad y listar apellido, nombre y DNI de cada patinador que 
        participó en el estilo dado. 
        
        2)Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador 
        que obtuvo el mayor puntaje en la evaluación. 
        Regla de negocio: El puntaje es el promedio de las 3 valoraciones dadas por los 
        jueces. Además, para resolver esta funcionalidad, el analista le solicita que 
        sobrecargueel operador “>”. 
        
        3) Listar los datos de los patinadores que participaron en estilo libre y en escuela.
        
        4) Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los 
        jueces. 
        
        0) Terminar con el programa.
        ''')
        opc = input("Eliga una opción y presione enter: ")
        os.system('cls')    
        if opc == '1':
            unMf.patinajeEstilo(listaE)
            os.system('cls') 
        elif opc == '2':
            unMf.mayorPuntaje(listaE)
            os.system('cls') 
        elif opc == '3':
            unMf.listarPatinadores(listaE)
            os.system('cls') 
        elif opc == '4':
            unMf.puntuacionP(listaE)
            os.system('cls') 

    print("Hasta la proxima!! :D")
    