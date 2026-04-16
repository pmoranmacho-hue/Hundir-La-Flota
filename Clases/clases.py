import numpy as np
import random


from Variables.variables import (
   board_size, ships,
   simbolo_empty, simbolo_ship,
   simbolo_hit, simbolo_miss, simbolo_sunk
)



#Excepción

class CeldaYaDisparadaError(Exception):
    """
    Se lanza cuando se intenta disparar a una celda que ya recibió un disparo.
    """


#Clase Tablero

class Tablero:
    """
    Representa el tablero de juego de un jugador en Hundir la Flota.
    """

    MAX_INTENTOS_COLOCACION = 1000

    def __init__(self, player_id: str):
        """
        Constructor: inicializa el tablero vacío para un jugador.

        Args:
            player_id: Identificador del jugador (p.ej. ``"humano"`` o ``"cpu"``).
        """
        self.player_id: str = player_id
        self.size: int = board_size
        self.board: np.ndarray = np.full((self.size, self.size), simbolo_empty)
        self.tracking: np.ndarray = np.full((self.size, self.size), simbolo_empty)
        self.barcos: list[list[tuple[int, int]]] = []  

    #Colocación de barcos

    def _coloca_barco(self, eslora: int) -> None:
        """
        Coloca un barco de la eslora indicada en una posición aleatoria válida.

        Args:
            eslora: Número de celdas que ocupa el barco.

        Raises:
            RuntimeError: Si no se encuentra posición válida tras
                ``MAX_INTENTOS_COLOCACION`` intentos.
        """
        orientaciones = ["horizontal", "vertical"]

        for _ in range(self.MAX_INTENTOS_COLOCACION):
            orient = random.choice(orientaciones)
            fila   = random.randint(0, self.size - 1)
            col    = random.randint(0, self.size - 1)

            coords = self._calcular_coordenadas(fila, col, eslora, orient)

            if self._coordenadas_validas(coords):
                for r, c in coords:
                    self.board[r, c] = simbolo_ship
                self.barcos.append(coords)             
                return

        raise RuntimeError(
            f"No se pudo colocar un barco de eslora {eslora} en el tablero "
            f"tras {self.MAX_INTENTOS_COLOCACION} intentos."
        )

    def place_ships(self) -> None:
        """
        Coloca todos los barcos definidos en el diccionario ``ships``.
        """
        for nombre_barco, info in ships.items():
            cantidad, eslora = info[0], info[1]
            for _ in range(cantidad):
                self._coloca_barco(eslora)

    #Recepción de disparos

    def receive_shot(self, fila: int, col: int) -> str:
        """
        Procesa un disparo entrante y actualiza el tablero propio.

        Args:
            fila: Índice de fila del disparo (0-indexado).
            col:  Índice de columna del disparo (0-indexado).

        Returns:
            ``"Hundido"``  si el disparo hunde el barco completo.
            ``"Tocado"``   si impacta pero el barco sigue a flote.
            ``"Agua"``  si es agua.

        Raises:
            IndexError:            Si las coordenadas están fuera del tablero.
            CeldaYaDisparadaError: Si esa celda ya recibió un disparo previo.
        """
        self._validar_coordenadas(fila, col)

        celda = self.board[fila, col]

        if celda in (simbolo_hit, simbolo_miss, simbolo_sunk):
            raise CeldaYaDisparadaError(
                f"La celda ({fila}, {col}) ya recibió un disparo anteriormente."
            )

        # Hay barco en la celda
        if celda == simbolo_ship:
            self.board[fila, col] = simbolo_hit
            for barco in self.barcos:
                if (fila, col) in barco:
                    if all(self.board[r, c] == simbolo_hit for r, c in barco):
                        for r, c in barco:
                            self.board[r, c] = simbolo_sunk
                        return "Hundido"
                    return "Tocado"

        # Agua
        self.board[fila, col] = simbolo_miss
        return "Agua"
        

    #Visualización

    def display(self, show_ships: bool = True) -> None:
        """
        Imprime el tablero en consola con cabeceras de fila y columna.

        Args:
            show_ships: Si es ``False``, oculta los barcos (útil para mostrar
                        el tablero propio al rival). Por defecto ``True``.
        """
        col_header = "   " + "  ".join(str(c) for c in range(self.size))
        separador  = "  +" + "---" * self.size + "+"

        print(f"\n  Tablero de '{self.player_id}'")
        print(col_header)
        print(separador)

        for r in range(self.size):
            fila_celdas = []
            for c in range(self.size):
                celda = self.board[r, c]
                if celda == simbolo_ship and not show_ships:
                    fila_celdas.append(simbolo_empty)
                else:
                    fila_celdas.append(celda)
            print(f"{r} | " + "  ".join(fila_celdas) + "  |")

        print(separador)

    def display_tracking(self) -> None:
        """
        Imprime el tablero de seguimiento (disparos realizados al rival).
        """
        col_header = "   " + "  ".join(str(c) for c in range(self.size))
        separador  = "  +" + "---" * self.size + "+"

        print(f"\n  Seguimiento de '{self.player_id}'")
        print(col_header)
        print(separador)

        for r in range(self.size):
            fila_celdas = [self.tracking[r, c] for c in range(self.size)]
            print(f"{r} | " + "  ".join(fila_celdas) + "  |")

        print(separador)

    #Auxiliares

    def _calcular_coordenadas(
            self, fila: int, col: int, eslora: int, orient: str
    ) -> list[tuple[int, int]]:
        if orient.lower() == "horizontal":
            return [(fila, col + i) for i in range(eslora)]
        return [(fila + i, col) for i in range(eslora)]

    def _coordenadas_validas(self, coords: list[tuple[int, int]]) -> bool:
        return all(
            0 <= r < self.size and 0 <= c < self.size and self.board[r, c] == simbolo_empty
            for r, c in coords
        )

    def _validar_coordenadas(self, fila: int, col: int) -> None:
        if not (0 <= fila < self.size and 0 <= col < self.size):
            raise IndexError(
                f"Coordenadas ({fila}, {col}) fuera del tablero de tamaño {self.size}x{self.size}."
            )