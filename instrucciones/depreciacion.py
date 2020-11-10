# Proyecto: Depreciación
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Calcular la depreciación de un activo
print("Bienvenido, calcularemos la depreciación de tu activo")

nombre = input("Ingresa el nombre de tu activo: ")

valor = input("Ingresa el precio de tu activo: ")
valor = float(valor)

print("""
Elige una categoría:
A. Equipo de cómputo
B. Maquinaria
C. Herramientas
""")

categoria = input("Elige una: ")

if categoria == 'A' or categoria == 'a':
  depreciacion = 0.333333

# de lo contrario si
elif categoria == 'B' or categoria == 'b':
  depreciacion = 0.2

elif categoria == 'C' or categoria == 'c':
  depreciacion = 0.25

val_depreciacion = valor * depreciacion

print(str(nombre) + " tiene una depreciación de " + str(val_depreciacion))