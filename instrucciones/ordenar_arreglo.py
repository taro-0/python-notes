# Proyecto: Ordenar
# Autor: Estuardo Díaz
# Carnet: 1324545-3
                           
def burbuja(numeros):
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
  
  return numeros
