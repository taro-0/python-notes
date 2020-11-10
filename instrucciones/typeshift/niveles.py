facil = ['colas', 'toros', 'agudo']
# , 'agata', 'Agita', 'rugby', 'yagas', 'pegar', 'salta', 'tonos', 'timon', 'limon', 'Bocas', 'pumas', 'letra', 'tenis', 'joyas', 'panty', 'hobby', 'mayas']
dificil = ['pelotas', 'cabello', 'cabañas', 'echamos', 'cabezal', 'gabacha', 'fabulas', 'xilemas', 'vaciado', 'ubicada', 'taberna', 'sabanas', 'toreada', 'peloton', 'sabados', 'rabanal', 'quebrar', 'quijada', 'pachuco', 'pacayas']  
muy_dificil = ['danig', 'desactivar', 'buscador', 'medicina', 'abejorro', 'gabachas', 'siquinala', 'barberena', 'colores', 'botellas', 'moderno', 'confiable', 'volcanes', '', 'espacios', 'penales', 'piochas', 'internet', 'témperas', 'movistar']

def elegir_nivel():
  nivel = input('''
  Elige un nivel

  1. Facil
  2. Dificil
  3. Muy Dificil

  ''')

  if nivel == '1':
    return facil
  elif nivel == '2':
    return dificil
  else:
    return muy_dificil
