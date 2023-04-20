disponivel = float(input())
valores = 0
cont = 0

while disponivel > valores:
  val = float(input())
  valores += val
  cont += 1

  if valores > disponivel:
    valores -= val
    cont -= 1
    break
    
v = disponivel - valores
print('Número de itens', cont)
print('Saldo: %.2f' % v)