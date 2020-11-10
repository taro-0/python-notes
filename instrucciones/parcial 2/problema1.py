# Estuardo Diaz
#

num1 = input('Ingrese un número: ')
num1 = int(num1)

num2 = input('Ingrese otro número: ')
num2 = int(num2)

for i in range(num1, num2 + 1):
  if (i % 6 == 0):
    print(i)

