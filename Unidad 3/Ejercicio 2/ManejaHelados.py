from Helado import Helado
class ManejaHelado:
    def __init__(self):
        self.__listahelados=[]

    def cargar_helado(self,listasabor):
        print("1- 100gr")
        print("2- 150gr")
        print("3- 250gr")
        print("4- 500gr")
        print("5- 1000gr")
        tipohelado=input("Ingrese el tipo de helado:\n")
        if tipohelado=="1":
            gramos=100
            precio=300
        elif tipohelado=="2":
            gramos=150
            precio=400
        elif tipohelado=="3":
            gramos=250
            precio=700
        elif tipohelado=="4":
            gramos=500
            precio=1300
        elif tipohelado=="5":
            gramos=1000
            precio=2500
        cantisabores=int(input("Ingrese la cantidad de sabores para el helado (Máximo 4):\n"))
        heladoaux=Helado(gramos,precio)
        for i in range (cantisabores):
            nomsab=input("Ingrese el nombre del sabor {} elegido\n".format(i+1))
            heladoaux.cargar_sabores(listasabor,nomsab)
        self.__listahelados.append(heladoaux)
    
    def estimar_gramos(self,id):
        totalgramos=0
        for fila in self.__listahelados:
            totalgramos+=fila.get_gramos(id)
        print ("El total de gramos del helado es: {}".format(totalgramos))
    
    def mostrar_por_tipohelados(self,tipohelado):
        if tipohelado=="1":
            gramos=100
        elif tipohelado=="2":
            gramos=150
        elif tipohelado=="3":
            gramos=250
        elif tipohelado=="4":
            gramos=500
        elif tipohelado=="5":
            gramos=1000
        print ("Los helados que se han vendido en ese tamaño son:")
        for fila in self.__listahelados:
            if gramos==fila.get_gramo():
                fila.mostrar_sabores()
    
    def calcular_total(self):
        gramos=[100,150,250,500,1000]
        contador=[0,0,0,0,0]
        for fila in self.__listahelados:
            if gramos[0]==fila.get_gramo():
                contador[0]+=fila.get_precio()
            elif gramos[1]==fila.get_gramo():
                contador[1]+=fila.get_precio()
            elif gramos[2]==fila.get_gramo():
                contador[2]+=fila.get_precio()
            elif gramos[3]==fila.get_gramo():
                contador[3]+=fila.get_precio()
            elif gramos[4]==fila.get_gramo():
                contador[4]+=fila.get_precio()
        print ("El total por cada tipo de helado es:")
        print ("Para el helado de {}gr: {}$".format(gramos[0],contador[0]))
        print ("Para el helado de {}gr: {}$".format(gramos[1],contador[1]))
        print ("Para el helado de {}gr: {}$".format(gramos[2],contador[2]))
        print ("Para el helado de {}gr: {}$".format(gramos[3],contador[3]))
        print ("Para el helado de {}gr: {}$".format(gramos[4],contador[4]))
        
    def mostrar_helados(self):
        for i,fila in enumerate(self.__listahelados):
            print ("\nDatos del helado "+str(i+1))
            fila.mostrar()