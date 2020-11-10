# Proyecto: Bucle
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# 'hola'
# ['h','o','l','a']

lista_palabras = ['Perro', 'Gato', 'Elefante', 'Hormiga', 'Águila', 'Pulpo']

animal = input('Escribe un animal: ')

# El animal esta en la lista de palabras
if animal in lista_palabras:
  print('¡Ohh! Ese animal me gusta a mi también')
else:
  print('Ese animal no lo conocía')