# Proyecto: Operandos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos diferentes operaciones con números
print('¡Hola! Estamos evaluando si dos numeros son divisibles entre si')

a = input('Ingresa el valor de A: ')
a = int(a)

b = input('Ingresa el valor de B: ')
b = int(b)

mod1 = b % a
mod2 = a % b

# valor de verdad
# Doble igual sirve para evaluar si dos numeros son iguales
# Mod1 es igual a 0?
val1 = (mod1 == 0)

# Mod2 es igual a 0?
val2 = (mod2 == 0)
print('B es divisible entre A?', val1)
print('A es divisible entre B?', val2)