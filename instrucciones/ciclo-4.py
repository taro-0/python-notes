# Proyecto: Ciclos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos diferentes operaciones con números
suma = 0

# Range va a devolver un rango, que empieza
# en num_1 y termina en el num_2 menos 1
# range(1, 10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(5):
  num = input("Ingrese un número: ")
  num = int(num)

  # suma = suma + num
  suma += num

print("La suma de todos los números es:", suma)
