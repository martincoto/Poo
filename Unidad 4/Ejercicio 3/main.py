from Interfaz import Aplicacion
from Cotizacion import Cambio
if __name__ == "__main__":
    cotiz=Cambio()
    cotiz.obtener_cotizacion()
    app=Aplicacion(cotiz.get_cotizacion())