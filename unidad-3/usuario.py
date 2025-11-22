# Aqui se aplica la abstraccion y la interfaz:
# mostrar_info() obliga a las clases hijas a implementarlo

from abc import ABC, abstractmethod


# Se declara Usuario como clase abstracta heredado de ABC
# la clase Usuario seria la casa de astracta porque aqui se define
# lo que los usuarios deben tener, sin importar sus implementaciones
# funcionando como molde para las clases hijas
# ademas de no poder utilizarse directamente se obliga a utilizar el
# metodo de mostrar_info() a las hijas
class Usuario(ABC):

    # Constructor con atributos comunes para todas las clases hijas
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    # Se indica el Metodo abstracto:
    # interfaz obligatoria
    @abstractmethod
    def mostrar_info(self) -> str:

        # se usa como relleno para que el metodo exista pero no haga nada
        pass
