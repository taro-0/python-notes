# Proyecto: Cumpleaños
# Autor: Estuardo Díaz
# Carnet: 1324545-3

numeros = [1,45,24,66,98, 67,78,134,27,35,99,67,6]

# Ordena los numeros de menor a mayor
# En palabras ordena en orden alfabetico
numeros.sort()

# Ordena los numeros de mayor a menor
# En palabras ordena en orden alfabetico descendente
numeros.sort(reverse=True)

# Le da vuelta al arreglo
# ej.: [6,99,35,27,134,78,67,66,24,45,1]
numeros.reverse()

# Elimina el elemento en la posicion dada
# Importante el numero es la posicion
numeros.pop(2)

# Eliminar un elemento en especifico
# Importante el numero es el elemento a eliminar
# Elimina el primero que encuentre
numeros.remove(67)

# Para saber la posición de un elemento
# Devuelve la posición del primero que encuentre
numeros.index(67)
numeros.index('manzana')

# Para insertar un número
# Agrega un número en la posición indicada
# Primer numero es la posicion, segundo es el elemento
numeros.insert(4, 98)
numeros.insert(4, 'manzana')

# Elimina todos los elementos de un arreglo
numeros.clear()

# Nos devuelve la cantidad de veces que aparece
# un elemento en el arreglo
numeros.count(67)