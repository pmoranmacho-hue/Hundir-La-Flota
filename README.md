# 🚢 Hundir la Flota

Juego por turnos en Python para dos jugadores: tú contra la máquina.
Hunde todos los barcos del rival antes de que él hunda los tuyos.

---

## 📋 Requisitos

* Python 3.10 o superior
* Librería `numpy`

Instala la dependencia con:

```bash
pip install numpy
```

---

## 🚀 Cómo ejecutar el juego

1. Abre la terminal en VS Code con `Ctrl + ñ`
2. Navega a la carpeta del proyecto:

```bash
cd Hundir-La-Flota
```

3. Ejecuta el juego:

```bash
python main.py
```

---

## 📂 Estructura del proyecto

```bash
Hundir-La-Flota/
├── main.py              # Bucle principal del juego
├── auxiliar.py          # Funciones auxiliares (limpiar pantalla, etc.)
├── Clases/
│   ├── __init__.py
│   └── clases.py        # Clase Tablero
├── funciones/
│   ├── __init__.py
│   └── funciones.py     # Lógica de turnos y victoria
└── Variables/
    ├── __init__.py
    └── variables.py     # Constantes del juego
```

---

## 🎮 Reglas del juego

### Tablero

El juego se juega en un tablero de **10 x 10 posiciones** (filas y columnas del 0 al 9).

### Barcos

Cada jugador tiene los siguientes barcos colocados aleatoriamente al inicio:

| Barco        | Cantidad | Eslora |
| ------------ | -------- | ------ |
| Lancha       | 4        | 1      |
| Yate         | 3        | 2      |
| Submarino    | 2        | 3      |
| Portaaviones | 1        | 4      |

### Turnos

* Empiezas tú.
* En cada turno introduces una fila y una columna para disparar.
* Si aciertas (tocas un barco), **vuelves a disparar**.
* Si fallas (agua), le toca a la máquina.
* La máquina dispara de forma aleatoria.
* Si la máquina acierta, también repite turno.

### Victoria

Gana el jugador que hunda todos los barcos del rival primero.

---

## 🎯 Cómo disparar

El juego te pedirá las coordenadas por separado:

```
Introduce fila (0-9): 3
Introduce columna (0-9): 7
```

* Escribe solo un número en cada pregunta y pulsa Enter.
* No uses comas ni espacios.

---

## 🗺️ Símbolos del tablero

| Símbolo | Significado            |
| ------- | ---------------------- |
| _       | Agua sin disparar      |
| O       | Barco intacto          |
| X       | Tocado                 |
| ·       | Agua (disparo fallido) |
| S       | Hundido                |

---

## 👥 Equipo de desarrollo

Proyecto desarrollado como **Team Challenge del bootcamp de Data Science**.

| Rol | Responsabilidad | Nombre |
|-----|----------------|--------|
| Scrum Master | `variables.py` — constantes y estructura base | Pablo Morán |
| Dev 1 | `clases.py` — clase Tablero | Ana Belén Escobar |
| Dev 2 | `funciones.py` — lógica del juego | Jorge Rafael |
| Dev 3 | Funciones auxiliares | Lucía Vetrano |
| QA e Integration | Bucle principal e integración | Nil Coronado |
