class Producto:

    # Indicara cuantos productos se han creado
    contador_productos = 0

    # Constructor que inicializa cada producto con su nombre y precio
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

        # cada que se crea un producto el contador aumentara en 1
        Producto.contador_productos += 1

    # Metodo estatico: independiente de clase e instancia
    @staticmethod
    def es_precio_valido(precio: float) -> bool:

        # Solo valida que el precio sea mayor a cero
        return precio > 0

    # Metodo de clase donde recibe la ref. a la clase como parametro cls

    @classmethod
    def total_productos(cls) -> int:

        # Devuelve el valor actual del contador de productos creados
        return cls.contador_productos
