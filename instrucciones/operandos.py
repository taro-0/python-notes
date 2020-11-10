# Proyecto: Operandos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos diferentes operaciones con números
print('¡Hola! Estamos haciendo varias operaciones')

num_1 = input('Ingresa un número: ')
num_1 = int(num_1)

num_2 = input('Ingresa otro número: ')
num_2 = int(num_2)

num_3 = input('Ingresa un número más: ')
num_3 = int(num_3)

# Sumar dos números
suma = num_1 + num_2
print('La suma del primero y el segundo es: ', suma)

# Multiplicamos el primero y el segundo
mult = num_1 * num_2
print('La multiplicación del primero y el segundo es: ', mult)

# Dividimos el tercero y el primero
div = num_3 / num_1
print('La división del primero y el tercero es: ', div)

# Restamos los tres números
resta = num_1 - num_2 - num_3
print('La resta de los tres números es: ', resta)

# Elevar un número
exp = num_1 ** num_2
print('El primer número elevado al segundo es:', exp)

# Módulo - Operación que devuelve el residuo de una división
# 8 / 3 = 2.67
# El módulo sería 2
modulo = num_3 % num_1
print('El residuo de la división del primero y el tercero es:', modulo)

# División piso
# El resultado de una división aproximado a su resultado entero más cercano por
# debajo
piso = num_3 // num_1
print('El piso de la división del tercer y el primero es:', piso)