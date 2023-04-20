quant = int(input())

for monitorias in range(quant):
  nome = input()
  sem_u = int(input())
  sem_d = int(input())
  sem_t = int(input())
  sem_q = int(input())

  if sem_u >= 120 and sem_d >= 120 and sem_t >= 120 and sem_q >= 120:
    print(nome, 'tem monitorias OK! :-)')
  else:
    print(nome, 'não tem monitorias suficientes :-(')