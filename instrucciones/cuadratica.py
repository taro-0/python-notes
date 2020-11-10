# Proyecto: Operandos
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos diferentes operaciones con números
print('¡Hola! Estamos resolviendo una función cuadrática')

a = input('Ingresa el valor de A: ')
a = int(a)

b = input('Ingresa el valor de B: ')
b = int(b)

c = input('Ingresa el valor de C: ')
c = int(c)

# ax^2 + bx + c = 0
b_neg = -1 * b
exp = 1 / 2

# x2 = (-b + ((b^2 - 4ac) ^ 1/2)/2a
x1 = (b_neg + ((b**2) - 4*a*c) ** exp) / (2 * a)

# x1 = (-b - ((b^2) -     4ac) ^ 1/2)   /    2a
x2 = (b_neg - ((b**2) - 4*a*c) ** exp) / (2 * a)

print('X1 es: ', x1)
print('X2 es: ', x2)