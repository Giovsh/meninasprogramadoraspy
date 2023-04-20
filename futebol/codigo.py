timeUm = input()
timeDois = input()
golUm = int(input())
golDois = int(input())

if golUm > golDois:
  print('vitoria:', timeUm)
  
if golDois > golUm:
  print('vitoria:', timeDois)
  
elif golUm == golDois:
  print('prorrogação!')

  pro = int(input())
  pro2 = int(input())
  
  if pro > pro2:
    print('vitoria:', timeUm)
  
  if pro2 > pro:
    print('vitoria:', timeDois)
  
  if pro == pro2:
    print('disputa de penaltis!')