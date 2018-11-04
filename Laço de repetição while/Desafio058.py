#Desafio 058

from random import randint

pc = randint(0,10)
k = 1

user = int(input('TENTATIVA {}: '.format(k)))

while user != pc:
    k += 1
    user = int(input('TENTATIVA {}: '.format(k)))


print('TOTAL DE TENTATIVAS: {}'.format(k))