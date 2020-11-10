# Proyecto: Fibonacci
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Crearemos una secuencia de fibonacci

# 0 1 1 2 3 5 8 13 21 34
print("Secuencia fibonnacci")

# Entradas
# El total de números que queremos mostrar
total = input("¿Cuántos números quieres mostrar?: ")
total = int(total)

# Proceso
# Calcular el total de números en la secuencia fibonacci
fib0 = 0
fib1 = 1

for i in range(total):
  fib = fib0
  fib0 = fib1
  fib1 = fib + fib1

  print(fib)
