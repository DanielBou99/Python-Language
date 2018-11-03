#Desafio 054

from datetime import datetime

now = datetime.now()
nowyear = now.year

Pmaiores, Pmenores = 0,0

for i in range (0,7):
    ano = int(input('Ano de nascimento: '))
    if nowyear - ano < 18:
        Pmenores += 1
    else:
        Pmaiores += 1
print('Pessoas que atingiram a maioridade: {}'.format(Pmaiores))
print('Pessoas que ainda NÃO atingiram: {}'.format(Pmenores))
