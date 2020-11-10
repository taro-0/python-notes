# Proyecto: Ciclos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos listas de elementos
lista_palabras = ['Perro', 'Gato', 'Elefante', 'Hormiga', 'Águila', 'Pulpo']

for animal in lista_palabras:
  print("¿Te gusta este animal? ", animal)
  repuesta = input('si/no ')

  if repuesta == 'no':
    print("¡Hmmmm! lo siento :'(")
    break