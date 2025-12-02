# Se importa el modulo logging para registrar mensajes de depuracion
import logging

# configuracion basica de logging:
# > establece el nivel minimo de mensajes a mostrar
# > define el formato de salida de cada mensaje
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


# definicion de la funcion validar_datos
# retorna un booleano indicando si los datos son validos o no
def validar_datos(nombre=None, edad=None, correo=None) -> bool:

    # Inicia el bloque para validar entradas
    try:

        # Se crea una lista para acumular errores encontrados
        errores = []

        # ===> Validacion de nombre <===
        # verifica si el nombre no fue proporcionado
        if nombre is None:
            errores.append("Falta el nombre.")
        # verifica que el nombre sea una cadena de texto
        elif not isinstance(nombre, str):
            errores.append("El nombre debe ser únicamente texto.")
        # elimina espacios y verifica que no este vacio
        elif nombre.strip() == "":
            errores.append("El nombre no puede estar vacío.")

        # ===> Validacion de edad <===
        # verifica si la edad no fue proporcionada
        if edad is None:
            errores.append("Falta la edad.")
        # verifica que la edad sea un numero entero
        elif not isinstance(edad, int):
            errores.append("La edad debe ser un número entero.")
        # verifica que la edad sea mayor que cero
        elif edad <= 0:
            errores.append("La edad debe ser mayor que cero.")

        # ===> Validacion de correo <===
        # verifica si el correo no fue proporcionado
        if correo is None:
            errores.append("Falta el correo.")
        # verifica que el correo sea una cadena de texto
        elif not isinstance(correo, str):
            errores.append("El correo debe contener solo texto.")
        # verifica que el correo contenga @
        elif "@" not in correo:
            errores.append("Debes ingresar una cuenta de correo valida.")

        # ===> Resultado de validacion <===
        # si existen errores se recorren y se muestran todos
        if errores:
            for err in errores:
                logging.error(f"{err}")
            # retorna False indicando que los datos no son validos
            return False

        # si no hay errores se informa que los datos son correctos
        logging.info("Datos validados correctamente.")
        # retorna True indicando que los datos son validos
        return True

    # captura errores de tipo:
    # cuando el dato no es del tipo esperado
    except TypeError as te:
        logging.error(f"Error de tipo: {te}")
        return False

    # captura errores de valor:
    # cuando el dato es del tipo correcto pero con valor invalido
    except ValueError as ve:
        logging.error(f"Error de valor: {ve}")
        return False

    # captura errores de division:
    # cuando se intenta dividir entre cero
    except ZeroDivisionError as zde:
        logging.error(f"Error de division: {zde}")
        return False

    # captura de cualquier otra excepcion no prevista
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        return False

    # bloque que siempre se ejecuta ocurra o no excepcion
    finally:
        logging.debug("Finalizando validacion.")
