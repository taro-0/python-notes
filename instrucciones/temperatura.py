# Proyecto: Temperatura
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Calcular Si la sensación térmica es fría o cálida
print("Bienvenido")

temperatura = input("¿Cuál es la temperatura de hoy?")
temperatura = int(temperatura)

# Congelado - -1C
if temperatura < 0:
  print("Brrrr ¡Me Congelo!!")
# Frío - 10C
elif temperatura <= 16:
  print("Uhh, que rico el frío")
# Cálido - 30C
elif temperatura < 30:
  print("¡Que buen clima hace hoy!")
elif temperatura < 40:
  print("¡Que calor!")
# Me quemo - 40
else:
  print("¡¡Me quemo!!")