# Proyecto: Cumpleaños
# Autor: Estuardo Díaz
# Carnet: 1324545-3
from random import shuffle

# Shuffle sirve para ordenar
# elementos de un arreglo de forma aleatoria
lista_palabras = ['Perro', 'Gato', 'Elefante', 'Hormiga', 'Aguila', 'Pulpo']

# Ordeno las palabras y las muestro
lista_palabras.sort()
print(*lista_palabras, sep=",")

# Se ordenan aleatoriamente y las muestro
shuffle(lista_palabras)
print(*lista_palabras, sep=",")

# Una cadena es un conjunto de simbolos
# Una cadena es un arreglo de símbolos
#        012345678901234567890
frase = 'Hola yo soy una frase'

# Convierte una frase en una lista de simbolos
frase = list(frase)