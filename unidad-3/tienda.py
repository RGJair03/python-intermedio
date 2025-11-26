# Agregacion: Tienda contiene ventas, pero estas
# pueden existir fuera de la tienda
from venta import Venta


class Tienda:

    # Constructor que inicializa la tienda con un nombre
    def __init__(self, nombre):

        # Guarda el nombre de la tienda
        self.nombre = nombre

        # Lista donde se almacenaran unicamente las ventas confirmadas
        self.ventas = []

    # Método para registrar una venta en la tienda
    def registrar_venta(self, venta: Venta):

        # Se intenta confirmar la venta antes de registrarla
        mensaje = venta.confirmar()

        # Si el mensaje indica confirmacion, se agrega la venta a la lista
        if "Venta confirmada" in mensaje:
            self.ventas.append(venta)

        # Devuelve el mensaje de confirmacion o de error
        return mensaje
