class Ventana:
    __titulo = ''
    __xsup = 0
    __ysup = 0
    __xinf = 0
    __yinf = 0
    def __init__(self, titulo, xs=0, xi=0, ys = 100, yi = 100):
        self.__titulo = titulo
        if xs < xi and ys < yi:
            if xs > -1:
                self.__xsup = xs
            if ys > -1:
                self.__ysup = ys
            if xi < 501:
                self.__xinf = xi
            if yi < 501:
                self.__yinf = yi
    def getTitulo(self):
        return(self.__titulo)
    def alto(self):
        return(self.__xsup - self.__ysup)
    def ancho(self):
        return(self.__xinf - self.__yinf)
    def mostrar(self):
        print("Ventana : ", self.__titulo)
        print("Coordenadas: ({},{}), ({},{})".format(self.__xsup, self.__ysup, self.__xinf, self.__yinf))
        return
    def moverDerecha(self,derecha=1):
        self.__xsup += derecha
        self.__xinf += derecha
        if self.__xinf > 500:
            self.__xsup -= self.__xinf - 500
            self.__xinf = 500
        return
    def moverIzquierda(self,izquierda=1):
        self.__xsup -= izquierda
        self.__xinf -= izquierda
        if self.__xsup < 0:
            self.__xinf += -self.__xsup
            self.__xsup = 0
        return
    def bajar(self, bajar=1):
        self.__ysup += bajar
        self.__yinf += bajar
        if self.__yinf > 500:
            self.__ysup -= self.__yinf - 500
            self.__xinf = 500
        return
    def subir(self, subir=1):
        self.__ysup -= subir
        self.__yinf -= subir
        if self.__xsup < 0:
            self.__yinf += -self.__ysup
            self.__ysup = 0
        return

