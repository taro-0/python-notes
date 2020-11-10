# Estuardo Diaz
#

numeros = [-5, 1.1, 0, -2000, 7, 4, 189, 130.5, 75, -50, 1, 2, 3, 4, -4, -3, -2, -1, 12, 2000]

pares = []
impares = []

# opcional
# numeros.sort()
n = len(numeros)
for i in range(n - 1):
  for j in range(0, n - i - 1):
    num1 = numeros[j]
    num2 = numeros[j + 1]

    # Ordenar de menor a mayor
    if num1 > num2:
      # cambia la posición
      numeros[j] = num2
      numeros[j + 1] = num1


for num in numeros:
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)


print('Numeros pares')
print(*pares, sep=',')

print('Numeros impares')
print(*impares, sep=',')
