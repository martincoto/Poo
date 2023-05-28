class Evaluacion():
    __dni=''
    __estilo=''
    __valoracion=[]
    
    def __init__(self,dni,estilo,valor=[]):
        self.__dni=dni
        self.__estilo=estilo
        self.__valoracion=valor
    
    def getEstilo(self):
        return self.__estilo
    
    def calculoProm(self):
        return (self.__valoracion[1]+self.__valoracion[2]+self.__valoracion[0])/3
    
    def __gt__(self,maxp):
        aux=self.calculoProm()
        if (aux)>maxp:
            return aux
        else:
            return maxp
        

    def mostrarDatos(self):
       # for i in range(len(self.__valoracion)):
        #    print(self.__valoracion[i])
        print("{} {} {} {} {}".format(self.__dni,self.__estilo,self.__valoracion[0],self.__valoracion[1],self.__valoracion[2]))
    
    def mostrarDatos4(self):
        print("Las notas son: ")
        print("{} {} {}".format(self.__valoracion[0],self.__valoracion[1],self.__valoracion[2]))