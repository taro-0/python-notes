# Estuardo Diaz
#

# empleados = []
# sueldos = []

cantidad_empleados = 0

cantidad_empleados = input('¿Cuántos empleados ingresará?: ')
cantidad_empleados = int(cantidad_empleados)

for i in range(cantidad_empleados):
  empleado = input('Ingrese el nombre del empleado: ')
  
  horas = input('Ingrese la cantidad de horas que '+  empleado + ' trabajó: ')
  horas = float(horas)

  sueldo = horas * 7.5
  
  empleados.append(empleado)
  sueldos.append(sueldo)


for j in range(cantidad_empleados):
  mensaje = empleados[j] + ': Q' + str(sueldos[j])
  print(mensaje)