from collections import Counter, OrderedDict

compras = {
    1: "Baruch",
    2: "Jair",
    3: "Lizbeth",
    4: "Jonathan",
    5: "Mariana",
    6: "Sebastian",
    7: "Cesar",
    8: "Eduardo",
    9: "Yesica",
    10: "Holly",
    11: "Jair",
    12: "Lizbeth",
    13: "Sebastian",
    14: "Cesar",
    15: "Lissette",
    16: "Lissette",
}

registrados = {
    1: "Lizbeth",
    2: "Jonathan",
    3: "Sebastian",
    4: "Mariana",
    5: "Cesar",
    6: "Eduardo",
    7: "Yesica",
    8: "Fabiola",
    9: "Holly",
    10: "Baruch",
}

# 1 -> Clientes nuevos
clientes_nuevos = set(compras.values()) - set(registrados.values())

# 2 -> Clientes por orden de compra
clientes_ordenados = {}
contador = 1
for cliente in OrderedDict.fromkeys(compras.values()):
    clientes_ordenados[cliente] = contador
    contador += 1

# 3 -> Resumen de clientes frecuentes
conteo = Counter(compras.values())

# 4 -> Resumen de compras mayor a 1 vez
resumen = {c: f"Ha comprado {n} veces" for c, n in conteo.items() if n > 1}

# === Mostrar resultados ===
print("\nClientes nuevos no registrados:")
print(clientes_nuevos)

print("\nClientes por orden de compra:")
print(clientes_ordenados)

print("\nResumen por cliente frecuente:")
print(resumen)
