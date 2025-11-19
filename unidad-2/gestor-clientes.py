from collections import Counter, OrderedDict


def obtener_nombres(compras):
    # recorre compras y toma la clave de cada diccionario
    return [list(c.keys())[0] for c in compras]


def clientes_nuevos(compras, registrados):
    # Se obtiene la lista de nombres
    nombres = obtener_nombres(compras)
    # Se aplica la diferencia de set para ver cuales no estan en registrados
    return set(nombres) - set(registrados.keys())


def orden_clientes(compras):
    orden = OrderedDict()
    # recorre compras con indice desde 1
    for i, compra in enumerate(compras, start=1):
        # obtener el nombre del cliente
        cliente = list(compra.keys())[0]
        # si el cliente no esta en orden
        if cliente not in orden:
            # agrega cliente con su indice
            orden[cliente] = i
    return dict(orden)


def contar_compras(compras):
    nombres = obtener_nombres(compras)
    # aplicamos Counter para contar ocurrencias
    return Counter(nombres)


def resumen_compras(compras):
    conteo = contar_compras(compras)
    resumen = {}
    # recorre cada cliente y su numero de compras
    for cliente, veces in conteo.items():
        # valida que tenga mas de una compra
        if veces > 1:
            clave = f"Ha comprado {veces} veces"
            # obtiene la lista existente o crea una lista vacia
            lista = resumen.get(clave, [])
            # agrega el cliente a la lista
            lista.append(cliente)
            # guarda la lista actualizada en el diccionario
            resumen[clave] = lista
    return resumen


def reporte(compras, registrados):
    print("\n=== Reporte de Clientes ===")
    print("\nClientes nuevos no registrados:")
    print(clientes_nuevos(compras, registrados))
    print("\nDiccionario de clientes unicos (orden numerico):")
    print(orden_clientes(compras))
    print("\nResumen por cliente frecuente (solo mas de una compra):")
    print(resumen_compras(compras))


def main():

    # lista de compras con clientes e ID del producto que adquirieron
    compras = [
        {"Cesar": 1},
        {"Lizbeth": 3},
        {"Mariana": 1},
        {"Holly": 1},
        {"Holly": 1},
        {"Yesica": 1},
        {"Jair": 2},
        {"Cesar": 1},
        {"Lizbeth": 2},
        {"Jair": 3},
        {"Yesica": 3},
        {"Cesar": 1},
        {"Lissette": 1},
        {"Carlos": 2},
        {"Lizbeth": 2},
        {"Luis": 1},
        {"Luis": 2},
        {"Luis": 3},
    ]

    # clientes registrados
    registrados = {
        "Lizbeth": "registrado",
        "Cesar": "registrado",
        "Baruch": "registrado",
        "Jonathan": "registrado",
        "Mariana": "registrado",
        "Eduardo": "registrado",
        "Holly": "registrado",
    }

    reporte(compras, registrados)


main()
