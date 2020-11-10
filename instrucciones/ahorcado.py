# Proyecto: Cumpleaños
# Autor: Estuardo Díaz
# Carnet: 1324545-3
from random import randint
from screen import clear
from time import sleep

palabras = ['guitarra', 'bateria', 'cancion', 'album', 'letra', 'ritmo', 'entonacion', 'timmy', 'tommy']

play = True
wins = 0
loses = 0

while play:
  # Generamos una palabra al azar
  num = randint(0, len(palabras) - 1)
  palabra = palabras[num]

  # Hacemos un arreglo de guiones y lo mostramos
  total_letras = len(palabra)
  guiones = ['-'] * total_letras
  letras = []
  vidas = 5
  adivinadas = 0

  # letra
  # xyluip
  while vidas > 0:
    # Mostramos los guiones
    print(*guiones, sep='')
    print(*letras, sep=',')

    letra = input('Escribe una letra: ')

    letras.append(letra)
    # Evaluamos La letra está en la palabra
    if letra not in palabra:
      vidas -= 1
      print('ups! Fallaste')
    # Si está, entonces reemplazamos los guiones
    else:
      print('Correcto')
      adivinadas += palabra.count(letra)
      for i in range(total_letras):
        if palabra[i] == letra:
          guiones[i] = letra
    
    if '-' not in guiones:
      print('¡Ganaste!')
      print('La palabra es:', palabra)
      wins += 1
      clear()
      break

    if vidas == 0:
      loses += 1
      clear()
      print('Perdiste!!')

    sleep(1.5)
    clear()

  eleccion = input('¿Seguir jugando? s/n: ')
  play = (eleccion == 's' or eleccion == 'si')


print('Ganaste {} veces'.format(wins))
print('Perdiste {} veces'.format(loses))