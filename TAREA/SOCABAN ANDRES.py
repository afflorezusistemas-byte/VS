
import os

# =========================
# MAPAS DEL JUEGO
# =========================

niveles = [

    # Nivel 1
    [
        list("#######"),
        list("#     #"),
        list("#  $  #"),
        list("# .@  #"),
        list("#     #"),
        list("#######")
    ],

    # Nivel 2
    [
        list("########"),
        list("#   .  #"),
        list("#   $  #"),
        list("#   @  #"),
        list("#      #"),
        list("########")
    ],

    # Nivel 3
    [
        list("########"),
        list("# .    #"),
        list("# $    #"),
        list("# $ @  #"),
        list("#      #"),
        list("########")
    ],

    # Nivel 4
    [
        list("#########"),
        list("# .   . #"),
        list("# $   $ #"),
        list("#   @   #"),
        list("#       #"),
        list("#########")
    ],

    # Nivel 5
    [
        list("#########"),
        list("#   .   #"),
        list("#   $   #"),
        list("#   @   #"),
        list("#  ###  #"),
        list("#########")
    ],

    # Nivel 6
    [
        list("##########"),
        list("# .    . #"),
        list("# $    $ #"),
        list("#    @   #"),
        list("#        #"),
        list("##########")
    ],

    # Nivel 7
    [
        list("##########"),
        list("#   .    #"),
        list("# ###$   #"),
        list("#   @    #"),
        list("#        #"),
        list("##########")
    ],

    # Nivel 8
    [
        list("###########"),
        list("# .     . #"),
        list("# $ ### $ #"),
        list("#    @    #"),
        list("#         #"),
        list("###########")
    ],

    # Nivel 9
    [
        list("###########"),
        list("#   .     #"),
        list("#   $     #"),
        list("# ###@    #"),
        list("#         #"),
        list("###########")
    ],

    # Nivel 10
    [
        list("############"),
        list("# .      . #"),
        list("# $      $ #"),
        list("#     @    #"),
        list("#          #"),
        list("############")
    ],

    # Nivel 11
    [
        list("############"),
        list("# . . .    #"),
        list("# $ $ $    #"),
        list("#    @     #"),
        list("#          #"),
        list("############")
    ],

    # Nivel 12
    [
        list("#############"),
        list("# .   #   . #"),
        list("# $   #   $ #"),
        list("#     @     #"),
        list("# .   #   . #"),
        list("# $   #   $ #"),
        list("#############")
    ]
]

# =========================
# FUNCION PARA LIMPIAR
# =========================

def limpiar():

    os.system("cls" if os.name == "nt" else "clear")


# =========================
# DIBUJAR MAPA
# =========================

def dibujar_mapa(matriz):

    limpiar()

    for fila in matriz:
        print("".join(fila))

    print("\nControles:")
    print("W = Arriba")
    print("S = Abajo")
    print("A = Izquierda")
    print("D = Derecha")
    print("Q = Salir")


# =========================
# POSICION DEL JUGADOR
# =========================

def obtener_posicion_jugador(matriz):

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            if matriz[i][j] == "@":
                return i, j


# =========================
# FUNCION PARA MOVER
# =========================

def mover(matriz, direccion):

    fila, columna = obtener_posicion_jugador(matriz)

    # movimientos
    df = 0
    dc = 0

    if direccion == "w":
        df = -1

    elif direccion == "s":
        df = 1

    elif direccion == "a":
        dc = -1

    elif direccion == "d":
        dc = 1

    else:
        return

    nueva_fila = fila + df
    nueva_columna = columna + dc

    # evitar errores
    if nueva_fila < 0 or nueva_columna < 0:
        return

    if nueva_fila >= len(matriz):
        return

    if nueva_columna >= len(matriz[0]):
        return

    destino = matriz[nueva_fila][nueva_columna]

    # pared
    if destino == "#":
        return

    # caja
    if destino == "$":

        caja_fila = nueva_fila + df
        caja_columna = nueva_columna + dc

        if caja_fila < 0 or caja_columna < 0:
            return

        if caja_fila >= len(matriz):
            return

        if caja_columna >= len(matriz[0]):
            return

        siguiente = matriz[caja_fila][caja_columna]

        # mover caja
        if siguiente == " " or siguiente == ".":

            matriz[caja_fila][caja_columna] = "$"
            matriz[nueva_fila][nueva_columna] = " "

        else:
            return

    # mover jugador
    matriz[fila][columna] = " "
    matriz[nueva_fila][nueva_columna] = "@"



# =========================
# VERIFICAR SI GANO
# =========================

def gano(matriz):

    for fila in matriz:

        if "$" in fila:
            return False

    return True


# =========================
# JUEGO
# =========================

for numero in range(len(niveles)):

    mapa = [fila[:] for fila in niveles[numero]]

    while True:

        dibujar_mapa(mapa)

        print("\nNivel:", numero + 1)

        if gano(mapa):

            print("\nGanaste este nivel")
            input("Presiona ENTER para seguir...")
            break

        tecla = input("\nMovimiento: ").lower()

        if tecla == "q":

            print("\nJuego terminado")
            exit()

        mover(mapa, tecla)

print("\nFelicidades completaste todos los niveles")

