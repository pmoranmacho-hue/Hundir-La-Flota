from Variables.variables import messages, simbolo_empty, simbolo_hit, simbolo_miss, simbolo_sunk
import os


def limpiar_pantalla():
    # Limpiamos pantalla para evitar que se acumulen cosas y se vea más limpio
    os.system('cls' if os.name == 'nt' else 'clear') # esto nos permite que sea compatible (creo que esta correcto)


def mostrar_turno(turno):
    # Mostramos de quién es el turno actual
    if turno == "jugador":
        print(messages["player_turn"])
    else:
        print(messages["cpu_turn"])


def pedir_coordenadas():
    # Pedimos al usuario que introduzca las coordenadas del disparo
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
    # Validamos que el disparo no haya sido realizado antes, para evitar que el jugador o la CPU disparen a la misma coordenada más de una vez.
    # True si el disparo es válido, False si ya se disparó ahí.
    if (fila, columna) in disparos_previos:
        print(messages["already_shot"])
        return False
    return True


def mostrar_resultado(resultado):
    # Mostramos el resultado del disparo (hit, miss o sunk).
    if resultado == "hit":
        print(messages["shot"])
    elif resultado == "miss":
        print(messages["miss"])
    elif resultado == "sunk":
        print(messages["sunk"])
    