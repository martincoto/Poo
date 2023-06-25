import requests
class Cambio:
    def __init__(self):
        self.__cotiz=0.0
    
    def obtener_cotizacion(self):
        response=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        datos=response.json()
        cotizacion_str = datos[0]['casa']['venta']
        self.__cotiz = float(cotizacion_str.replace(',', '.'))
    
    def get_cotizacion(self):
        return self.__cotiz
    
if __name__ == "__main__":
    cam=Cambio()
    cam.obtener_cotizacion()