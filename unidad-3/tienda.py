# Agregacion: Tienda contiene ventas, pero estas
# pueden existir fuera de la tienda
from venta import Venta


class Tienda:

    # Este constructor inicializa la tienda con su nombre y una lista de ventas
    def __init__(self, nombre: str):

        self.nombre = nombre

        # Lista que almacenara las ventas registradas en la tienda
        self.ventas: list[Venta] = []

    # Metodo para registrar una venta en la tienda
    def registrar_venta(self, venta: Venta) -> None:

        # Agrega la venta recibida a la lista de ventas
        self.ventas.append(venta)
