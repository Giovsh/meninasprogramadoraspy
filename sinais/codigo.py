lista = ['4paus','7copas','Aespadas','7ouros', '3paus','3copas','3espadas','3ouros']

numero = input()
carta = input()

manilha = numero + carta

if manilha in lista[0]:
  print('olho')
elif manilha in lista[1]:
  print('testa')
elif manilha in lista[2]:
  print('bochecha')
elif manilha in lista[3]:
  print('lábio')
elif manilha in lista[4]:
  print('ombro')
elif manilha in lista[5]:
  print('ombro')
elif manilha in lista[6]:
  print('ombro')
elif manilha in lista[7]:
  print('ombro')
else:
  print('nada')