# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos una historia con datos
# ingresados por el usuario

nombre_per = input('Escribe tu nombre: ')
edad_per = input('Escribe tu edad: ')

frase = 'Me llamo {nombre} y tengo {edad} años'

print(frase.format(nombre = nombre_per, edad = edad_per ))