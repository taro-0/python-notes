# Proyecto: Piedra papel o tijera
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Juego de piedra papel o tijera
from random import randint

from screen import clear

while True:
  # 1 - Piedra
  # 2 - Papel
  # 3 - Tijera
  juego_pc = randint(1, 3)

  # Muestro las opciones al jugador
  print("""
  1. Piedra
  2. Papel
  3. Tijera
  """)

  eleccion_jugador = input("Elige una: ")
  eleccion_jugador = int(eleccion_jugador)

  if juego_pc == 1:
    print("La pc escogió piedra")
  elif juego_pc == 2:
    print("La pc escogió papel")
  else:
    print("La pc escogió tijeras")


  if juego_pc == eleccion_jugador:
    print("¡Es un empate!")
  elif eleccion_jugador == 2 and juego_pc == 1:
    print("¡Tu ganas!")
  elif eleccion_jugador == 3 and juego_pc == 2:
    print("¡Tu ganas!")
  elif eleccion_jugador == 1 and juego_pc == 3:
    print("¡Tu ganas!")
  else:
    print("Perdiste :(")

  otro = input('¿Jugar de nuevo? si/no: ')

  if otro == 'no':
    break
  else:
    clear()