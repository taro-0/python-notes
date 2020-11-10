# Proyecto: Pato Ganso
# Autor: Estuardo Díaz
# Carnet: 1324545-3

numeros = [1,45,24,66,67,78,134,27,35,99,6]
length = len(numeros)

for i in range(length):
  num = numeros[i]

  if num % 2 == 0:
    numeros[i] = 'pato'
  else:
    numeros[i] = 'ganso'

print(*numeros, sep='-')