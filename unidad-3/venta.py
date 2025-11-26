from producto import Producto
from cliente import Cliente


class Venta:

    # Constructor que recibe un cliente para asociarlo a la venta
    def __init__(self, cliente: Cliente):

        # Guarda la referencia al cliente de esta venta
        self.cliente = cliente

        # Composicion: Venta contiene productos, sin ellos
        # no existiria la venta, los productos son parte escencial de la venta
        # y esta almacena objetos de tipo Producto creando la composicion
        self.productos: list[Producto] = []

        # Bandera para saber si la venta ya fue confirmada
        self.confirmada = False

    # Metodo para agregar un producto a la venta
    def agregar_producto(self, producto: Producto) -> None:

        # se inserta un producto al final de la lista de productos
        self.productos.append(producto)

    # Metodo para calcular el total de la venta
    def total(self) -> float:

        # Suma el precio de cada producto usando una comprension generadora
        return sum(p.precio for p in self.productos)

    def confirmar(self):

        # Si ya fue confirmada, no vuelve a descontar
        if self.confirmada:
            return "Venta ya confirmada anteriormente"

        total = self.total()

        # Si el saldo no alcanza, no descuenta ni confirma
        if self.cliente.saldo < total:
            return "Saldo insuficiente para realizar la compra"

        # Si alcanza, descuenta y marca como confirmada
        self.cliente.saldo -= total
        self.confirmada = True
        return f"Venta confirmada. Nuevo saldo: ${self.cliente.saldo}"
