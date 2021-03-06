# tablero
# mostrar el tablero
# empezamos el juego
# turnos
  # pedirle la posici贸n a la persona
  # verificamos que no est茅 ocupada esa celda
  # marcar esa posici贸n
# verificar si alguien gan贸
  # ver si tenemos 3 simbolos en una fila
  # si tenemos 3 simbolos en una misma columna
  # si tenemos 3 simbolos en un diagonal
# verificar si hay empate
# cambio el jugador

# esto es una lista, un vector 馃檧 array
tablero = [ "-", "-", "-", 
            "-", "-", "-",
            "-", "-", "-" ]

def mostrar_tablero():
  print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
  print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
  print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

# ejecutar la funci贸n
mostrar_tablero()

seguir_jugando = True

jugador_activo = "馃惐"

posicion = ""

# null
ganador = None

def turno():
  global tablero, jugador_activo, posicion

  print("Es el turno de: " + jugador_activo)

  posicion = ""

  valido = False

  while not valido:
    posicion = input("Eleg铆 una posici贸n del 1 al 9: ")

    posicion = int(posicion) - 1

    if tablero[posicion] == "-":
      valido = True
    else:
      print("Esa posici贸n est谩 ocupada")
  
  tablero[posicion] = jugador_activo

  mostrar_tablero()


def verificar_columnas():
  global seguir_jugando, ganador

  col_1 = tablero[0] == tablero[3] == tablero[6] != "-"
  col_2 = tablero[1] == tablero[4] == tablero[7] != "-"
  col_3 = tablero[2] == tablero[5] == tablero[8] != "-"

  if col_1 == True or col_2 == True or col_3 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_filas():
  global seguir_jugando, ganador

  fil_1 = tablero[0] == tablero[1] == tablero[2] != "-"
  fil_2 = tablero[3] == tablero[4] == tablero[5] != "-"
  fil_3 = tablero[6] == tablero[7] == tablero[8] != "-"

  if fil_1 == True or fil_2 == True or fil_3 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_diagonales():
  global seguir_jugando, ganador

  dia_1 = tablero[0] == tablero[4] == tablero[8] != "-"
  dia_2 = tablero[2] == tablero[4] == tablero[6] != "-"

  if dia_1 == True or dia_2 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_empate():
  global seguir_jugando

  if "-" not in tablero:
    seguir_jugando = False

while seguir_jugando == True:
  turno()
  
  verificar_columnas()
  verificar_filas()
  verificar_diagonales()
  verificar_empate()

  if jugador_activo == "馃惐":
    jugador_activo = "馃檧"
  else:
    jugador_activo = "馃惐"

if ganador == "馃惐" or ganador == "馃檧":
  print("Gan贸 " + ganador)
else:
  print("Empate")
