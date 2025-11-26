from cliente import Cliente
from producto import Producto
from venta import Venta
from tienda import Tienda

# Crear cliente con saldo inicial
cliente1 = Cliente("Luis", "luis@mail.com", 800)

# Crear productos
p1 = Producto("Teclado", 250)
p2 = Producto("Mouse", 150)

# Crear venta y agregar productos
venta1 = Venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)

# Crear tienda
tienda = Tienda("TechStore")

# Mostrar informacion inicial del cliente
print(
    f"Cliente: {cliente1.nombre}, Correo: {cliente1.correo}, Saldo: ${cliente1.saldo:.2f}"
)

# Mostrar total de la venta
print(f"Total de la venta: ${venta1.total():.2f}")

# Registrar venta en la tienda (confirma y descuenta saldo si alcanza)
mensaje = tienda.registrar_venta(venta1)
print(mensaje)

# Mostrar cuantas ventas se registraron en la tienda
print(f"Ventas registradas: {len(tienda.ventas)}")
