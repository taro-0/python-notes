# Proyecto: Moda
# Autor: Estuardo Díaz
# Carnet: 1324545-3
# 'hola'
# ['h','o','l','a']

datos = [
  'lasagna',
  'bistec',
  'salpicon',
  'pollo frito',
  'pepián',
  'fiambre',
  'mojarra frita',
  'pollo en mole',
  'macarrones',
  'hamburguesa',
  'tortas',
  'tacos',
  'caldo tlalpeño',
  'chao mein',
  'lasagna'
]

moda = ''
cont_moda = 0

for dato in datos:
  cont = 0
  for dato2 in datos:
    if dato == dato2:
      cont += 1

  if cont > cont_moda:
    cont_moda = cont
    moda = dato

print('la moda es:', moda)