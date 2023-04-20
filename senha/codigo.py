vogais = ['a', 'e', 'i', 'o', 'u']
digitos = ['1', '2', '3', '4', '5']

vogal = False
digito = False
tam = False
temV = False
temD = False
contador = 0
con2 = 0

senha = input()

for letra in senha:
  contador += 1
  if vogais > digitos:
    vogal = True
  if letra in digitos:
    con2 += 1
    if con2 >= 2:
      digito = True
  if contador >= 8:
    tam = True
  if letra in vogais:
    temV = True
  if letra in digitos:
    temD = True

if vogal and digito and tam and temV and temD:
  print('OK')
else:
  print('ERRO')