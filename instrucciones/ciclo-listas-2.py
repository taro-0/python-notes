# Proyecto: Ciclos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos listas de elementos
lista_palabras = ['Perro', 'Gato', 'Elefante', 'Hormiga', 'Águila', 'Pulpo']

te_gustan = []
no_te_gustan = []

for palabra in lista_palabras:
  print("¿Te gusta este animal? ", palabra)
  repuesta = input('si/no ')

  if repuesta == 'no':
    no_te_gustan.append(palabra)
    print("¡Hmmmm! lo siento :'(")
  else:
    te_gustan.append(palabra)
    print('¡Cool!')

print('Te gustan: ')
print(*te_gustan, sep=', ')

print('No te gustan: ')
print(*no_te_gustan, sep=', ')