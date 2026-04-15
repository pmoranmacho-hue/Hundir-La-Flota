

#Tamaño del tablero

board_size = 10

# Barcos

#He marcado primer value (número de barcos) y segundo value (tamaño del mismo)

ships = {
    "lancha":      [4, 1],  
    "yate":        [3, 2],  
    "submarino":   [2, 3],  
    "portaaviones":[1, 4],  
}

#Cantidas de barcos que participan y celdas que ocupan

total_ships = 10
total_ships_cells = 20

#Diccionario de mensajes

messages = {
    #Bievenida y inicio de juego
    "welcome": "¡Bienvenido al juego Hundir la Flota!",

  # turnos
  "player_turn": "Tu turno. Introduce disparo:",
  "cpu_turn": "Turno de tú rival",

  # resultados
  "shot": "¡Tocado! Vuelves a disparar.",
  "miss": "Agua. Le toca a tu rival.",
  "sunk": "¡Hundido!",
  "cpu_hit": "Tu rival te ha dado.",
  "cpu_miss": "Tu rival ha fallado.",
  "cpu_sunk": "Tu rival ha hundido un barco.",

  # errores
  "invalid_coords": "Disparo erróneo. Malas coordenadas. Inténtalo de nuevo.",
  "already_shot": "Ya disparaste ahí. Inténtalo de nuevo.",
}

#Símbolos del tablero

simbolo_empty = "_" # parte de tablero sin disparar
simbolo_ship = "O" # barco nuestro
simbolo_hit = "X" # tocado
simbolo_miss = "·" # agua (disparo fallido)
simbolo_sunk = "S" # hundido (he usado S, por ser la abreviatura de sunk)
