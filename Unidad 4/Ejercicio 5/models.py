class Movie(object):
	def __init__(self,titulo,resumen,lenguaje_original,fecha_lanzamiento):
		self.__titulo = titulo
		self.__resumen = resumen
		self.__lenguaje_original = lenguaje_original
		self.__fecha_lanzamiento = fecha_lanzamiento
		self.__generos = []

	def Carga_Genero(self,generoId):
		self.__generos.append(generoId)
  
	def getTitulo(self):
		return self.__titulo

	def getResumen(self):
		return self.__resumen

	def getLenguaje(self):
		return self.__lenguaje_original

	def getFecha(self):
		return self.__fecha_lanzamiento

	def getGeneros(self):
		return self.__generos