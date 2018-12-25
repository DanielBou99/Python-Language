'''
Programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em
ordem, sabendo que o vencedor tirou o maior numero no dado.
'''

from random import randint
from operator import itemgetter
from time import sleep

dic = {}

for i in range(1,5):
    nome = 'jogador' + str(i)
    dado = randint(1,6)
    dic[nome] = dado

dic = sorted(dic.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(dic,1):
    print(f'{i}º Lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
