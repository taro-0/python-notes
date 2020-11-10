# Proyecto: Índice de Masa Corporal
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Calcular el índice de masa corporal de una persona

print("¡Bienvenidos! Vamos a calcular el IMC")

altura = input("Ingrese su altura en metros: ")
# Convierte simbolos a decimales
altura = float(altura)

peso = input("Ingrese su peso en KG: ")
peso = float(peso)

imc = peso / (altura ** 2)

# Si el imc es mayor ó igual a 25
if imc >= 25:
  print("El paciente se encuentra en sobrepeso")
# de lo contrario
else:
  print("El paciente se encuentra en su peso normal")

