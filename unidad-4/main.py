from registro import validar_datos


def probar_validaciones():

    # lista de casos de entradas validas e invalidas
    casos = [
        ("Jair", 30, "jair@gmail.com"),  # caso valido
        ("", 25, "beth@gmail.com"),  # nombre vacio
        ("Holly", -5, "holly@gmail.com"),  # edad negativa
        ("Jesus", "veinte", "jesus@gmail.com"),  # edad no entera
        ("Liz", 22, "liz.gmail.com"),  # correo sin @
        ("Raul", "correo@gmail.com"),  # falta edad
        ("Juan", 20),  # falta correo
        ("Jorge",),  # falta edad y correo
        (25,),  # solo edad
    ]

    # recorre cada caso de la lista para probarlo
    for caso in casos:

        try:

            # desempaquetado segun la longitud de la tupla
            if len(caso) == 3:
                # si hay 3 valores se asignan directo a nombre, edad y correo
                nombre, edad, correo = caso

            elif len(caso) == 2:
                # si hay 2 valores se analiza el segundo
                nombre, segundo = caso
                if isinstance(segundo, int):
                    # si el segundo es entero se toma como edad y falta correo
                    edad, correo = segundo, None
                else:
                    # si el segundo no es entero se toma como correo y falta edad
                    edad, correo = None, segundo

            elif len(caso) == 1:
                # si hay 1 valor se analiza su tipo
                unico = caso[0]
                if isinstance(unico, int):
                    # si es entero se toma como edad y faltan nombre y correo
                    nombre, edad, correo = None, unico, None
                elif isinstance(unico, str):
                    # si es cadena se toma como nombre y faltan edad y correo
                    nombre, edad, correo = unico, None, None
                else:
                    # si no es ni cadena ni entero se marca invalido
                    raise ValueError("Formato invalido")

            else:
                # si la tupla no tiene valores se marca invalido
                raise ValueError("Formato invalido")

            # muestra en consola que caso se esta probando
            print(f"\nProbando: {nombre}, {edad}, {correo}")
            # llama a la funcion validar_datos y guarda el resultado
            resultado = validar_datos(nombre, edad, correo)
            # informa si el resultado fue correcto o incorrecto
            print("Resultado:", "Correcto" if resultado else "Incorrecto")

        # captura cualquier error que ocurra en la ejecucion de pruebas
        except Exception as e:
            print(f"Error en caso {caso}: {e}")


# punto de entrada para ejecutar las pruebas directamente desde este archivo
if __name__ == "__main__":
    # ejecuta la funcion
    probar_validaciones()
