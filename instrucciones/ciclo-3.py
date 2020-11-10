# Proyecto: Ciclos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos diferentes operaciones con números
num_1 = input("ingrese un número: ")
num_1 = int(num_1)

num_2 = input("ingrese otro número: ")
num_2 = int(num_2)

# Range va a devolver un rango, que empieza
# en num_1 y termina en el num_2 menos 1
# range(1, 10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(num_1, num_2 + 1, 2):
  print(i)