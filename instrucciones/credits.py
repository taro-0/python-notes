# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos una historia con datos
# ingresados por el usuario

nombre = input('Escribe el nombre de una persona: ')
pelicula = input('Escribe el nombre de una pelicula: ')

director = 'Presentado por: \'{nombre} inventino\''

title = pelicula.strip().upper().center(80,'*')
formato = director.format(nombre = nombre).center(80)

print(title)
print(formato)
print('*' * 80)