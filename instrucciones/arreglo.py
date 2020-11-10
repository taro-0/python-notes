# Proyecto: Cumpleaños
# Autor: Estuardo Díaz
# Carnet: 1324545-3

# Arreglo: Conjunto de elementos contiguos
# Varios elementos que están guardados uno al lado del otro
# En python los arreglos y listas son lo mismo

# Arreglo vacío
arreglo = []

# Arreglo con números
# Posición: 0 - 1 -2 -3- 4- 5 - 6   
numeros = [1, 2, 4, 8, 9, 12, 5]

# Arreglos de palabras
# Posición:    0       1        2         3
palabras = ['Hola', 'Adios', 'Jueves', 'Progra']

# Largo - length arreglo
# cantidad de elementos
cantidad = len(palabras)

# Acceder a un elemento
# Ej.: 'Jueves'
elemento = palabras[2]

palabras[2] = 'Ayer'

for i in range(cantidad):
  elemento = palabras[i]
  print('El elemento en la posición ' + str(i) + ' es: ', elemento)