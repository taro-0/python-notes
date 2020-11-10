# Proyecto: Ciclos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos diferentes operaciones con números
cantidad = input("ingrese un número: ")
cantidad = int(cantidad)

# Range va a devolver un rango, que empieza
# en 0 y termina en el número que le enviamos menos 1
# range(10) -> 0 hasta 9
for i in range(cantidad):
  print(i + 1)