# Exercício
Joaninha tromba mas não cai
Quando a Joaninha é ligada, o programa captura da bateria um valor inteiro entre 0 e 100, correspondente à porcentagem de carga disponível
A Joaninha só funciona com carga mínima maior que 5%
Antes de cada movimento, o programa obtém informações de dois sensores. O primeiro sensor informa B de bateu ou L se a área livre à frente. O segundo sensor informa A se tem um Abismo, ou P se há Piso para avançar
Para controlar a Joaninha, seu programa emite os comandos virar, em caso de necessidade, ou avançar, sempre que possível. Quando não há bateria disponível para trabalhar, seu programa avisa que é hora de recarregar.  Junto com cada comando, seu sempre programa informa o quanto de bateria resta na Joaninha.
Cada movimento de avançar consome 1% de bateria. Cada movimento de virar consome  5% de bateria.

#### Entrada
Primeira linha: um valor inteiro entre 0 e 100
A seguir, um número indeterminado de pares de linhas com uma letra cada
1. O primeiro valor do par contém B ou L
2. O segundo valor do par contém A ou P

#### Saída
Enquanto houver carga mínima na bateria suficiente, a joaninha avança ou vira, de acordo com os dados obtidos dos sensores
Ao final, o programa informa a porcentagem de bateria restante. 

###### Exemplo de entrada
50
B
P
B

###### Exemplo de saída

virar: 45
virar: 40
virar: 35