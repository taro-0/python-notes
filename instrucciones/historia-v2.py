# Proyecto: Instrucciones
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos una historia con datos
# ingresados por el usuario

nombre_per = input('Escribe el nombre de una persona: ')
animal_per = input('Escribe el nombre de un animal: ')
pais_per = input('Escribe el nombre de un país o ciudad: ')

# Placeholder: Variable o simbolo que toma el lugar de
# el valor final en la cadena
historia = 'Una persona llamada {nombre} viajó a {pais}, en el avión su acompañante era un {animal}'

input('Presiona enter para ver tu historia')

formato = historia.format(nombre = nombre_per, pais = pais_per, animal = animal_per)
print(formato)