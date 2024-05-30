# Tema - Teoría de Conjuntos - Relaciones y Funciones
# Propiedades de las Relaciones

# Reflexiva
# Simétrica
# Antisimétrica
# Transitiva
# Relación de Orden
# Relación de Equivalencia

# conjunto_A = {1, 2, 3}
# relacion_reflexiva = {(1, 1), (2, 2), (3, 3)}
# relacion_simetrica = {(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)}
# relacion_antisimetrica = {(1, 2), (2, 3), (1, 3)}
# relacion_transitiva = {
#     (1, 2),
#     (2, 3),
#     (1, 3),
#     (3, 1),
#     (2, 1),
#     (1, 1),
#     (2, 2),
#     (3, 2),
#     (3, 3),
# }


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
    # Convertimos en lista la relación para tener acceso a las posiciones de los pares ordenados
    l_relacion = list(relacion)

    # Con la siguiente variable nos posicionamos en el primer elemento (par ordenado) de la lista
    i = 0

    # El objetivo es comparar cada elemento de la lista con los demas uno a uno, es decir, el primer elemento lo analizamos con cada elemento consecutivo a el hasta llegar al final de la lista. Una vez no hay con quién comparar, seguimos con el siguiente elemento.
    # i se encargará de ser el primer elemento a comparar
    # j serán todos los elementos de la lista para compararlos uno a uno

    # Se recorre por primera vez la lista
    while i < len(l_relacion):
        # Con la siguiente variable nos posicionamos en el segundo elemento (par ordenado) de la lista
        j = 1

        # Recorremos por segunda vez la lista a partir del segundo elemento en adelante.
        while j <= len(l_relacion) - 1:
            # Asignamos nuestras variables para comparar
            w = l_relacion[i][0]
            x = l_relacion[i][1]

            y = l_relacion[j][0]
            z = l_relacion[j][1]

            # Comparamos el segundo elemento del primer par ordenado con el primer elemento del segundo par ordenado
            # La definición de la propiedad transitiva en teoría de conjuntos es:
            # R es transitiva si:
            #   ∀ x, y, z ∈ R : [(x, y) ∧ (y, z) ∈ R] → (x, z) ∈ R
            # A fines de prácticos 'y' de la definición matemática es 'x' e 'y' en el algoritmo
            if x == y:
                print(f"{(w,x)} y {(y,z)} => {(w,z)} pertenece a la Relación?")

                # Si (w,z) no está en la Relación
                if (w, z) not in l_relacion:
                    print(f"{(w,x)} y {(y,z)} => {(w,z)} no pertenece en la Relación")

                    return False
                else:
                    # Respuesta del primer print.
                    print(f"{w,z} SI pertenece a la Relación")

            # Incrementamos la variable para realizar las consecutivas comparaciones
            j = j + 1

        # Incrementamos la variable para continuar con el siguiente par ordenado fijo a comparar
        i = i + 1

    # Si sale del bucle es porqué la relación es transitiva
    return True
