# Proyecto: Cumpleaños
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# Este programa encuentra la edad de una persona en base a su fecha de nacimiento

from datetime import date

# La fecha de hoy
hoy = date.today()

# Obtener el día de hoy
dia = hoy.day

# Mes obtener el mes de hoy
mes = hoy.month

# Obtener el año de hoy
year = hoy.year

# Obtener los datos de la persona
print('¡Hola! Vamos a calcular tu edad')

# Obtener el día de nacimiento de la persona
dia_nac = input('¿Cuál es el día de la fecha de tu nacimiento?: ')
dia_nac = int(dia_nac)

# Obtener el mes de nacimiento de la persona
mes_nac = input('¿Cuál es el mes de la fecha de tu nacimiento?: ')
mes_nac = int(mes_nac)

# Obtener el año de nacimiento de la persona
year_nac = input('¿En qué año naciste?: ')
year_nac = int(year_nac)

diff_year = year - year_nac

# String - Cadena - str
print('Tienes ' + str(diff_year) + ' años')
