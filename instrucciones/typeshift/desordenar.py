from random import shuffle

def cambiar_palabra(palabra):
  nueva_palabra = list(palabra)
  shuffle(nueva_palabra)

  return nueva_palabra