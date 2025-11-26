# Se importa la clase abstracta de Usuario desde el archivo usuario.py
from usuario import Usuario


# Herencia: Administrador hereda de Usuario
class Administrador(Usuario):

    # Recibe los atributos de la clase padre y agrega uno extra: permisos
    def __init__(self, nombre: str, correo: str, permisos: list[str]):

        # super() llama al constructor de la clase padre
        # para inicializar nombre y correo
        super().__init__(nombre, correo)

        # Atributo propio de la clase hija de Administrador
        self.permisos = permisos

    # Se implemente el metodo abstracto heredado
    def mostrar_info(self) -> str:

        # retorna la informacion formateada
        return f"Administrador: {self.nombre}, Correo: {self.correo}, Permisos: {', '.join(self.permisos)}"
