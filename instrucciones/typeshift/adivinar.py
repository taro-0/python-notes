from desordenar import cambiar_palabra

def adivinar_palabra(palabra):
  vidas = 7
  palabra_nueva = cambiar_palabra(palabra)

  # Seguiré preguntando mientras tenga vidas
  while vidas > 0:
    print(*palabra_nueva, sep="")
    adivinada = input('Adivina la palabra: ')

    # Termino el ciclo y aumento al marcador
    if adivinada == palabra:
      print('Muy bien!')
      return True
    else:
      vidas -= 1
      print('te equivocaste, tienes {} vidas'.format(vidas))
  
  return False