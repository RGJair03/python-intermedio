# Se importa la clase abstracta de Usuario desde el archivo usuario.py
from usuario import Usuario


# Herencia: Cliente hereda de Usuario
class Cliente(Usuario):

    # Recibe los atributos de la clase padre y agrega uno extra: saldo
    def __init__(self, nombre: str, correo: str, saldo: float):

        # super() llama al constructor de la clase padre
        # para inicializar nombre y correo
        super().__init__(nombre, correo)

        # Atributo propio de la clase hija de Cliente
        self.saldo = saldo

    # Se implemente el metodo abstracto heredado
    def mostrar_info(self) -> str:

        # retorna la informacion formateada
        return (
            f"Cliente: {self.nombre}, Correo: {self.correo}, Saldo: ${self.saldo:.2f}"
        )
