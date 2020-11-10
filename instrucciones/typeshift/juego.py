from niveles import elegir_nivel
from adivinar import adivinar_palabra

# Juego principal
while True:
  # Parte principal del juego
  # ...
  aciertos = 0
  palabras = elegir_nivel()

  # Recorro todas las palabras
  for palabra in palabras:
    # En cada palabra tengo 7 intentos
    resultado = adivinar_palabra(palabra)

    if resultado:
      aciertos += 1
    else:
      print('oops, esfuerzate mas')

  print('Tienes {} aciertos'.format(aciertos))

  #Al final preguntar si quiere jugar de nuevo
  respuesta = input('¿Jugar de nuevo? (si/no): ')
  if respuesta == 'no':
    break
