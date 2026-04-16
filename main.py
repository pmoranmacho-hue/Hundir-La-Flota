import os

from Clases.clases import Tablero
from Funciones import disparo_cpu, disparo_jugador, mostrar_estado_juego, verificar_ganador
from Variables.variables import messages


def limpiar_pantalla() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pausar() -> None:
    input("\nPulsa Enter para continuar...")


def inicializar_juego() -> tuple[Tablero, Tablero]:
    """Crea tableros y coloca los barcos de ambos jugadores."""
    player_board = Tablero("humano")
    cpu_board = Tablero("cpu")
    player_board.place_ships()
    cpu_board.place_ships()
    return player_board, cpu_board


def juego() -> None:
    """Bucle principal del juego."""
    player_board, cpu_board = inicializar_juego()
    turno_jugador = True

    while True:
        limpiar_pantalla()
        mostrar_estado_juego(player_board, cpu_board)

        if turno_jugador:
            repite_turno = disparo_jugador(player_board, cpu_board)
            pausar()
        else:
            repite_turno = disparo_cpu(cpu_board, player_board)
            pausar()

        if verificar_ganador(player_board, cpu_board):
            limpiar_pantalla()
            mostrar_estado_juego(player_board, cpu_board)
            pausar()
            break

        if not repite_turno:
            turno_jugador = not turno_jugador


if __name__ == "__main__":
    limpiar_pantalla()
    print(messages["welcome"])
    input("\nPulsa Enter para empezar...")
    juego()