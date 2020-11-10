# Proyecto: Control de flujos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribir un programa que pida 20 numeros

for i in range(20):
  num = input("Escribe un número: ")
  num = int(num)

  if num % 8 == 0:
    print("¡Adiós!")
    break
