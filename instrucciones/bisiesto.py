# Proyecto: Bisiesto
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Indicar cuando un año es bisiesto
print("Hola, vamos a averiguar si un año es bisiesto o no")

year = input("Ingresa un año: ")
year = int(year)

# Si, El modulo de year y 4 es diferente de 0?, entonces
if (year % 4) != 0:
  print("El año no es bisiesto")
# De lo contrario, entonces
else:
  #  ¿El año es divisible entre 400?
  divisible_400 = (year % 400)
  # ¿El año no es divisible entre 100?
  divisible_100 = (year % 100)

  if divisible_400 == 0 or divisible_100 != 0:
    print("El año es bisiesto")
  else:
    print("El año no es bisiesto")