from Variables.variables import messages, simbolo_empty, simbolo_hit, simbolo_miss, simbolo_sunk
import os


def limpiar_pantalla():
    """
    Limpia la pantalla de la terminal.
    Funciona tanto en Windows como en Mac/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_turno(turno):
    """
    Muestra de quién es el turno actual.

    Args:
        turno (str): 'jugador' o 'cpu'
    """
    if turno == "jugador":
        print(messages["player_turn"])
    else:
        print(messages["cpu_turn"])


def pedir_coordenadas():
    """
    Pide al jugador que introduzca coordenadas de disparo.

    Returns:
        tuple: (fila, columna) como enteros validados.
    """
    while True:
        try:
            fila = int(input("Introduce fila (0-9): "))
            columna = int(input("Introduce columna (0-9): "))
            if 0 <= fila <= 9 and 0 <= columna <= 9:
                return fila, columna
            else:
                print(messages["invalid_coords"])
        except ValueError:
            print(messages["invalid_coords"])


def validar_disparo(fila, columna, disparos_previos):
    """
    Valida que el disparo no haya sido realizado antes.

    Args:
        fila (int): Fila del disparo.
        columna (int): Columna del disparo.
        disparos_previos (list): Lista de tuplas con disparos anteriores.

    Returns:
        bool: True si el disparo es válido, False si ya se disparó ahí.
    """
    if (fila, columna) in disparos_previos:
        print(messages["already_shot"])
        return False
    return True


def mostrar_resultado(resultado):
    """
    Muestra el resultado de un disparo.

    Args:
        resultado (str): 'hit', 'miss' o 'sunk'
    """
    if resultado == "hit":
        print(messages["shot"])
    elif resultado == "miss":
        print(messages["miss"])
    elif resultado == "sunk":
        print(messages["sunk"])
    