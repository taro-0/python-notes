# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Escribiremos una historia con datos
# ingresados por el usuario

eleccion = input('¿Continuar? si/no: ')
# Normalizar: Un proceso mediante el cual
# las entradas de nuestro programa están en el formato que
# esperamos

# Elimina los espacios en blanco al inicio y al final de una cadena
eleccion = eleccion.strip()

# Convierte todas las letras en minusculas
eleccion = eleccion.lower()

# Convierte todas las letras en mayúsculas
eleccion = eleccion.upper()

# Convierte la primer letra en mayúscula
# 'hola soy una frase'
# 'Hola soy una frase'
eleccion = eleccion.capitalize()

# Convierte cada letra de una palabra en mayúscula
# 'hola soy una frase'
# 'Hola Soy Una Frase'
eleccion = eleccion.title()

# Cambia todas las letras mayúsculas por minúsculas y viceversa
# 'Hola soy unA frase'
# 'hOLA SOY UNa frase'
eleccion = eleccion.swapcase()

# Regresa una cadena centrada
eleccion = eleccion.center(20, ' ')
