"""
funciones.py
Funciones auxiliares para Hundir la Flota:
- Entrada de coordenadas
- Turnos de jugador y CPU
- Comprobación de victoria
- Impresión de tableros
"""

from variables import (
    messages,
    simbolo_hit, simbolo_miss, simbolo_sunk,
    simbolo_empty, simbolo_ship,
)

from clases import Tablero, CeldaYaDisparadaError


def imprimir_tablero(tablero, titulo: str | None = None) -> None:
    """
    Imprime un tablero (matriz numpy o lista de listas) con cabeceras.

    Args:
        tablero: Estructura 2D indexable [fila][col] o [fila, col].
        titulo:  Texto opcional a mostrar encima del tablero.
    """
    size = len(tablero)

    if titulo:
        print(f"\n{titulo}")

    # Cabecera de columnas
    print("   " + "  ".join(str(i) for i in range(size)))
    print("  +" + "---" * size + "+")

    for r in range(size):
        # Para numpy funciona tanto tablero[r][c] como tablero[r, c]
        fila = [tablero[r][c] for c in range(size)]
        print(f"{r} | " + "  ".join(fila) + "  |")

    print("  +" + "---" * size + "+")


def pedir_coordenadas(size: int) -> tuple[int, int]:
    """
    Pide coordenadas al usuario y valida que sean correctas.

    Args:
        size: Tamaño del tablero (para validar límites).

    Returns:
        Tupla (fila, col) válida dentro del tablero.
    """
    while True:
        entrada = input("Introduce coordenadas (fila columna): ").strip()
        partes = entrada.split()

        if len(partes) != 2:
            print(messages["invalid_coords"])
            continue

        try:
            fila = int(partes[0])
            col = int(partes[1])
        except ValueError:
            print(messages["invalid_coords"])
            continue

        if not (0 <= fila < size and 0 <= col < size):
            print(messages["invalid_coords"])
            continue

        return fila, col


def turno_jugador(jugador: Tablero, enemigo: Tablero) -> str:
    """
    Ejecuta el turno del jugador humano.

    - Muestra el tablero de seguimiento.
    - Pide coordenadas.
    - Dispara al tablero enemigo.
    - Actualiza el tracking del jugador.
    - Muestra mensajes según el resultado.

    Args:
        jugador: Tablero del jugador humano.
        enemigo: Tablero del rival (CPU).

    Returns:
        "Tocado", "Hundido", "Agua" o "repetido".
    """
    print("\n" + messages["player_turn"])
    jugador.display_tracking()

    fila, col = pedir_coordenadas(jugador.size)

    try:
        resultado = enemigo.receive_shot(fila, col)
    except CeldaYaDisparadaError:
        # Disparo a una celda ya usada
        print(messages["already_shot"])
        return "repetido"
    except IndexError:
        # Por si llegara una coordenada fuera de rango (defensivo)
        print(messages["invalid_coords"])
        return "repetido"

    # Actualizar tracking según resultado
    if resultado == "Tocado":
        jugador.tracking[fila, col] = simbolo_hit
        print(messages["shot"])
    elif resultado == "Hundido":
        jugador.tracking[fila, col] = simbolo_sunk
        print(messages["sunk"])
    else:  # "Agua"
        jugador.tracking[fila, col] = simbolo_miss
        print(messages["miss"])

    return resultado


def turno_cpu(cpu: Tablero, enemigo: Tablero) -> str:
    """
    Turno automático de la CPU.

    - Elige una celda aleatoria que no haya sido disparada antes.
    - Dispara al tablero del jugador.
    - Muestra mensajes según el resultado.

    Args:
        cpu: Tablero de la CPU.
        enemigo: Tablero del jugador humano.

    Returns:
        "Tocado", "Hundido" o "Agua".
    """
    import random

    print("\n" + messages["cpu_turn"])

    # Elegir una celda no disparada (ni X, ni ·, ni S)
    while True:
        fila = random.randint(0, cpu.size - 1)
        col = random.randint(0, cpu.size - 1)

        celda = enemigo.board[fila, col]
        if celda not in (simbolo_hit, simbolo_miss, simbolo_sunk):
            break

    resultado = enemigo.receive_shot(fila, col)

    if resultado == "Tocado":
        print(messages["cpu_hit"])
    elif resultado == "Hundido":
        print(messages["cpu_sunk"])
    else:
        print(messages["cpu_miss"])

    return resultado


def comprobar_victoria(tablero: Tablero) -> bool:
    """
    Comprueba si un jugador ha perdido todos sus barcos.

    Args:
        tablero: Tablero del jugador a comprobar.

    Returns:
        True si ya no queda ninguna celda con simbolo_ship en sus barcos.
    """
    for barco in tablero.barcos:
        # Si queda alguna celda con barco sin hundir → NO hay victoria
        if any(tablero.board[r, c] == simbolo_ship for r, c in barco):
            return False
    return True
