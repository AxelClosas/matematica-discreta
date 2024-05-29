def calcularProductoCartesiano(conjunto_uno, conjunto_dos):
    conjunto_parejas_ordenadas = set()
    for x in conjunto_uno:
        for y in conjunto_dos:
            conjunto_parejas_ordenadas.add((x, y))

    return conjunto_parejas_ordenadas


conjunto_A = {1, 2, 3, 4}
conjunto_B = {1, 2, 3, 4}

resultado = calcularProductoCartesiano(conjunto_A, conjunto_B)

print(f"A = {conjunto_A}")
print(f"B = {conjunto_B}")
print(f"Tamaño del conjunto A: {len(conjunto_A)}")
print(f"Tamaño del conjunto B: {len(conjunto_B)}")
print("\n")
print(f"A x B = {resultado}")
print(f"Tamaño de A x B: {len(resultado)}")
