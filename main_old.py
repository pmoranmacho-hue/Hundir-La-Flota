from Clases.clases import Tablero
from funciones import turno_cpu, turno_jugador, comprobar_victoria
from Variables.variables import messages
from auxiliar import limpiar_pantalla


def pausar() -> None:
    input("\nPulsa Enter para continuar...")


def inicializar_juego() -> tuple[Tablero, Tablero]:
    """Crea tableros y coloca los barcos de ambos jugadores."""
    player_board = Tablero("humano")
    cpu_board = Tablero("cpu")
    player_board.place_ships()
    cpu_board.place_ships()
    return player_board, cpu_board


def mostrar_estado_juego(player_board: Tablero) -> None:
    """Muestra el tablero propio y el tablero de seguimiento."""
    player_board.display(show_ships=True)
    player_board.display_tracking()



def juego() -> None:
    """Bucle principal del juego."""
    player_board, cpu_board = inicializar_juego()
    turno_jugador_activo = True

    while True:
        limpiar_pantalla()
        mostrar_estado_juego(player_board)

        if turno_jugador_activo:
            resultado = turno_jugador(player_board, cpu_board)
            if comprobar_victoria(cpu_board):
                limpiar_pantalla()
                mostrar_estado_juego(player_board)
                print("\n¡Has ganado!")
                pausar()
                break
        else:
            resultado = turno_cpu(cpu_board, player_board)
            if comprobar_victoria(player_board):
                limpiar_pantalla()
                mostrar_estado_juego(player_board)
                print("\nTu rival ha ganado.")
                pausar()
                break

        pausar()

        if resultado == "Agua":
            turno_jugador_activo = not turno_jugador_activo


if __name__ == "__main__":
    limpiar_pantalla()
    print(messages["welcome"])
    input("\nPulsa Enter para empezar...")
    juego()
