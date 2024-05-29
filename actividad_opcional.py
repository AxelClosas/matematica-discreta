# Tema - Teoría de Conjuntos - Relaciones y Funciones
# Propiedades de las Relaciones

# Reflexiva
# Simétrica
# Antisimétrica
# Transitiva
# Relación de Orden
# Relación de Equivalencia

conjunto_A = {1, 2, 3}
relacion_reflexiva = {(1, 1), (2, 2), (3, 3)}
relacion_simetrica = {(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)}
relacion_antisimetrica = {(1, 2), (2, 3), (1, 3)}
relacion_transitiva = {(1, 2), (2, 3), (1, 3), (3, 1), (2, 1), (1, 1), (2, 2)}


def esReflexiva(conjunto, relacion):
    for x in conjunto:
        if (x, x) not in relacion:
            return False

    return True


def esSimetrica(relacion):
    for pareja in relacion:
        x, y = pareja
        if (y, x) not in relacion:
            return False

    return True


def esAntisimetrica(relacion):
    for pareja in relacion:
        x, y = pareja
        if (y, x) in relacion:
            return False

    return True


def esTransitiva(relacion):
    lista_parejas = list(relacion)
    i = 0
    while i < len(lista_parejas):
        x, y = lista_parejas[i]
        print(x, y)

        if y == lista_parejas[i + 1][0]:
            print(y)
        else:
            print(lista_parejas[i + 1][0])
        i += 1

    return True


print(esReflexiva(conjunto_A, relacion_reflexiva))

print(esSimetrica(relacion_simetrica))

print(esAntisimetrica(relacion_antisimetrica))

esTransitiva(relacion_transitiva)
