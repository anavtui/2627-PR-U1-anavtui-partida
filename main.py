def calcular_resultados(aciertos: int, errores: int) -> tuple[int, int]:
    """
    Devuelve una tupla con el número total de preguntas respondidas y la puntuación obtenida, en ese orden.
    :param: aciertos
    :param: errores
    :return: total_preguntas
    :return: puntuacion
    """

    total_preguntas = aciertos + errores

    puntuacion = (3 * aciertos) - (1 * errores)

    return total_preguntas, puntuacion

def valorar_partida(puntuacion: int) -> int:
    """
    Devuelve un número entero que indica la posición del mensaje que se debe mostrar de VALORACION_PARTIDA
    :param: puntuacion
    :return: VALORACION_PARTIDA
    """

    if puntuacion < 10:
        VALORACION_PARTIDA = 0
    elif (puntuacion >= 10) and (puntuacion <= 19):
        VALORACION_PARTIDA = 1
    else:
        VALORACION_PARTIDA = 2

    return VALORACION_PARTIDA

def main():

    aciertos_entrada = int(input())
    errores_entrada = int(input())
    if (aciertos_entrada < 0) or (errores_entrada < 0):
        print("ERROR - valores incorrectos")
    else:
        salida_calcular_resultados = calcular_resultados(aciertos_entrada, errores_entrada)
        salida_valorar_partida = valorar_partida(salida_calcular_resultados[1])

        if salida_valorar_partida == 0:
            valoracion = "Sigue practicando"
        elif salida_valorar_partida == 1:
            valoracion = "Buen resultado"
        elif salida_valorar_partida == 2:
            valoracion = "Excelente"

        print("Preguntas respondidas: ", salida_calcular_resultados[0])
        print("Puntuación: ", salida_calcular_resultados[1])
        print("Valoración: ", valoracion)

if __name__ == "__main__":
    main()