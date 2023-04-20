bateria = int(input())

while bateria > 5:
  sensorU = input()
  sensorD = input()
  if sensorU == 'B' and sensorD == 'A':
    bateria -= 5
    print('virar:', bateria)
  elif sensorU == 'B' and sensorD == 'P':
    bateria -= 5
    print('virar:', bateria)
  elif sensorU == 'L' and sensorD == 'A':
    bateria -= 5
    print('virar:', bateria)
  elif sensorU == 'L' and sensorD == 'P':
    bateria -= 1
    print('avançar:', bateria)

print('recarregar:', bateria)