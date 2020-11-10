from random import randint

# Tener una lista de nombres y adjetivos
#              0,        1,            2,      3,      4
nombres = ['AFRODITA', 'AMATERASU', 'APOLO', 'ARES', 'BACO', 'BRAHMA', 'BAAL', 'BUDA', 'CHAAC', 'CERNURNNOS', 'DAVLIN', 'DEMETER', 'DIANA', 'EREN', 'ENKI', 'EOS', 'FAFNIR', 'FENRIR', 'FREYA', 'GANESHA', 'GEB', 'HEFESTO', 'HERA', 'HERMES', 'HORUS', 'IRIS', 'IZANAMI', 'IXBALANQUE', 'ISHTAR', 'JUPITER', 'JUNO', 'KHEPRI', 'KISHAR', 'KUKULKAN', 'LOKI', 'LETO', 'MARTE', 'MERCURIO', 'MORRIGAN', 'NEITH', 'NEPTUNO', 'NINTU', 'ODIN', 'OSIRIS', 'POSEIDON', 'PHAETHON', 'QUETZALCOALT', 'RAMA', 'RHEA', 'SHIVA', 'SOL', 'SET', 'TYR', 'THANATOS', 'THOTH', 'UZUME', 'UTU', 'VISHNU', 'VULCAN', 'VENUS', 'XIN', 'XIPE', 'YMIR', 'YAM', 'YARIJ', 'ZEUS', 'ZUKO']
adjetivos = ['VALIENTE', 'ALEGRE', 'EMO', 'VENGADOR', 'SOCIAL', 'ESPECIAL', 'PODEROS@', 'CRIKO@', 'AMABLE', 'TOSTAD@']

# 'a' - 'A'
# Pedir al usuario su nombre, edad y género
nombre = input('Escribe tu nombre: ')
nombre = nombre.upper()

edad = input('¿Cuántos años tienes?: ')
edad = int(edad)

print('''
Cuál es tu género:
1. Masculino
2. Femenino
3. Otro - Prefiero no decirlo
''')
genero = input()

# Iniciamos las variables con su valor original
inicial_usuario = nombre[0]
candidatos = []

# busco los nombres que empiezan con la misma inicial
for apodo in nombres:
  if apodo[0] == inicial_usuario:
    candidatos.append(apodo)

while True:
  # la función len da el total de elementos de una lista
  total_candidatos = len(candidatos)

  # Si no hay al menos un nombre que empiece con la inicial paramos
  if total_candidatos == 0:
    print('No hemos podido generar un nombre para ti')
    break
  
  # Generamos un número aleatorio y tomamos esa posición de la lista
  # de candidatos
  num = randint(0, total_candidatos - 1)
  nickname = candidatos[num]

  # Obtenemos el total de adjetivos disponibles
  total_adjetivos = len(adjetivos)

  # Obtenemos un número aleatorio y elegimos el adejtivo
  num = randint(0, total_adjetivos - 1)
  adjetivo = adjetivos[num]

  # Concatenación
  nombre_us = nickname + ' ' + adjetivo + ' ' + str(edad)

  # Creamos un mensaje predeterminado
  mensaje = 'okay {nombre}, tu nuevo nombre es {nickname}'
  print(mensaje.format(nombre = nombre, nickname = nombre_us))

  # Preguntamos si desea hacer un nuevo
  respuesta = input('¿Deseas generar uno nuevo? (s/n): ')
  if respuesta == 'n':
    # Terminamos el programa
    print('Hasta pronto', nombre_us, ':D')
    break