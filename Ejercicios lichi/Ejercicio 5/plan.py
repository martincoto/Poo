import csv
class PlanAhorro:
    __cod = ''
    __modelo = ''
    __version = ''
    __valor = ''
    __cuotas = 60
    __CantCuotasMin = 10
    def __init__(self, cod, modelo, version, importe):
        self.__cod = int(cod)
        self.__modelo = modelo
        self.__version = version
        self.__valor = float(importe)
    def __str__ (self):
        return "%s %s %s" %(self.__cod,self.__modelo,self.__version)
    def getValor(self):
        return (self.__valor)
    def getCuotas(self):
        return(self.__cuotas)
    def getCod(self):
        return(self.__cod)
    def getModelo(self):
        return(self.__modelo)
    def actualizaValor(self,importe):
        self.__valor = importe
    @classmethod
    def getCantCuotas(cls):
        return (cls.__CantCuotasMin)
    @classmethod
    def getCuotas(cls):
        return (cls.__cuotas)
    @classmethod
    def modificaCantCuotas(cls,CuotasLicitas):
        cls.__CantCuotasMin = CuotasLicitas

class ManejadorPlan:
    def __init__(self):
        self.__lista = []
    def agregarPlan(self,unPlan):
        self.__lista.append(unPlan)
    def testPlan(self):
        archivo = open('C:\\Users\\lisan\\OneDrive\\2° Año\\Programación Orientada a Objetos\\Unidad 2\\Ejercicio 5\\planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            cod = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            importe = float(fila[3])
            unPlan = PlanAhorro(cod,modelo,version,importe)
            self.agregarPlan(unPlan)
        archivo.close
        return
    def modificaValor(self):
        i = 0
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            importe = float(input('Ingrese nuevo valor: '))
            self.__lista[i].actualizaValor(importe)
        return
    def obtenerCuota(self,i):
        cuotas = self.__lista[i].getCuotas()
        valor = self.__lista[i].getValor()
        return ((valor/cuotas)+valor * 0.10)
    def mostrarPlanes(self,importe):
        i = 0
        for i in range(len(self.__lista)):
            if(importe > self.obtenerCuota(i)):
                print(self.__lista[i])
        return
    def obtenerCuotaLicita(self,i):
        cuota = self.obtenerCuota(i)
        cuotasLicitas = PlanAhorro.getCantCuotas() 
        return (cuota * cuotasLicitas)
    def mostrarMontos(self):
        i = 0
        for i in range(len(self.__lista)):
            print("Vehiculo:", self.__lista[i].getModelo())
            print("Monto: $", self.obtenerCuotaLicita(i))
        return
    def cambiarCuotas(self,codigo,cant):
        i = 0
        b = None
        while not b and i in range(len(self.__lista)):
            if(codigo == self.__lista[i].getCod()):
                self.__lista[i].modificaCantCuotas(cant)
                b = True
                print("Se modificaron las cuotas.")
            i+=1
        return