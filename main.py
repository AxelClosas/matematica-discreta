def run():
    # Tema - Teoría de Conjuntos - Relaciones y Funciones
    # Propiedades de las Relaciones

    # Tenemos el conjunto A
    conjunto_A = {1, 2, 3, 4}

    # Realizamos el producto cartesiano A x A
    producto_cartesiano_AxA = {(x, y) for x in conjunto_A for y in conjunto_A}

    # Mostramos la info del conjunto A
    print(f"A = {conjunto_A}")
    print(f"Tamaño del conjunto A: {len(conjunto_A)}")
    print("\n")

    # Mostramos el producto cartesiano A x A
    print(f"A x A = {producto_cartesiano_AxA}")

    # Definimos la relación R, donde x <= y
    # Lenguaje matemático - Teoría de Conjuntos
    # R = {(x,y) / (x,y) ∈ A ∧ x <= y}

    # Creamos el conjunto usando comprehension (comprensión - Viva lógica de predicados 😊)
    R = {(x, y) for x, y in producto_cartesiano_AxA if x <= y}
    print(f"R = {R}")

    # Definimos una serie de funciones que verifican las propiedades de las relaciones

    def esReflexiva(conjunto, relacion):
        # Por cada elemento del conjunto
        for x in conjunto:
            # Comprobamos si el par (x,x) existe en la relación
            if (x, x) not in relacion:
                # Sino, retorna Falso, es decir, no es Reflexiva
                return False
        # Retorna Verdadero si es Reflexiva
        return True

    def esSimetrica(relacion):
        # Por cada pareja en la relación
        for pareja in relacion:
            # Obtenemos los valores de x y
            x, y = pareja
            # Comparamos si el par (y,x) no pertenece a la relación
            if (y, x) not in relacion:
                # Si retorna Falso es porqué no es Simétrica
                return False
        # Retorna Verdadero si es Simétrica
        return True

    def esAntisimetrica(relacion):
        # Por cada par ordenado o pareja en la relación
        for pareja in relacion:
            # Obtenemos sus valores
            x, y = pareja
            # Si x es igual a y no habría problema, cumple la definición de Antisimétrica en teoría de conjuntos
            if x == y:
                return True
            # Si el par (y, x) existe en la relación, retorna Falso, dado que no es Ansimétrica
            if (y, x) in relacion:
                return False
        # Retorna Verdadero si es Antisimétrica
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
                # A fines prácticos 'y' de la definición matemática es 'x' e 'y' en el algoritmo
                if x == y:
                    # Para debug, descomentar el siguiente print.
                    # print(f"{(w,x)} y {(y,z)} => {(w,z)} pertenece a la Relación?")

                    # Si (w,z) no está en la Relación
                    if (w, z) not in l_relacion:
                        # Para debug, descomentar el siguiente print.
                        # print(f"{(w,x)} y {(y,z)} => {(w,z)} no pertenece en la Relación")

                        return False
                    # Para debug, descomentar el bloque else
                    # else:
                    #     # Respuesta del primer print.
                    #     print(f"{w,z} SI pertenece a la Relación")

                # Incrementamos la variable para realizar las consecutivas comparaciones
                j = j + 1

            # Incrementamos la variable para continuar con el siguiente par ordenado fijo a comparar
            i = i + 1

        # Si sale del bucle es porqué la relación es transitiva
        return True

    # Haciendo uso de las funciones definidades previamete, creamos una función para saber si nuestra relación R es Relación de Orden.

    # Se tiene que cumplir que la Relación sea REFLEXIVA, ANTISIMÉTRICA y TRANSITIVA.

    # Recibe como parametro el conjunto inicial y la relación para analizar
    def esRelacionDeOrden(conjunto, relacion):
        # Si la relación
        if (
            # Es Reflexiva
            esReflexiva(conjunto, relacion)
            # Y es Antisimétrica
            and esAntisimetrica(relacion)
            # Y es Transitiva
            and esTransitiva(relacion)
        ):
            # Entonces es Relación de Orden. Retorna Verdadero
            return True

        # No cumple alguna de las condiciones previstas.
        # Entonces no es Relación de Orden. Retorna Falso
        return False

    # Ejecutamos la función esRelacionDeOrden para comprobar si nuestra relación inicial es Relación de Orden
    print("\n\nLa relación R es Relación de Orden?.\n\n")
    if esRelacionDeOrden(conjunto=conjunto_A, relacion=R):
        print(f"R es Reflexiva?: {esReflexiva(conjunto=conjunto_A, relacion=R)}")
        print(f"R es Antisimétrica?: {esAntisimetrica(relacion=R)}")
        print(f"R es Transitiva?: {esTransitiva(relacion=R)}")

        print(f"\n\nLa relación R = {R}\n\nes Relación de Orden")
    else:
        print(f"R es Reflexiva?: {esReflexiva(conjunto=conjunto_A, relacion=R)}")
        print(f"R es Antisimétrica?: {esAntisimetrica(relacion=R)}")
        print(f"R es Transitiva?: {esTransitiva(relacion=R)}")
        print(f"\n\nLa relación R = {R}\n\nNo es Relación de Orden")


if __name__ == "__main__":
    run()
