class ManejaPersona:
    def __init__(self):
        self.__listapers=[]
        
    def cargar_persona(self,personaaux):
        self.__listapers.append(personaaux)
    
    def mostrar_personas(self):
        for persona in self.__listapers:
            print (persona)