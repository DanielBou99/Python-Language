#Desafio 028

from random import randint

NumSorteado = randint(0,5)

NumUser = int(input('Escolha um numero entre 0 e 5:\n>>>'))

if NumSorteado == NumUser:
    print('Acertou!!')
else:
    print('Errou!!')

print('Numero sorteado: {}'.format(NumSorteado))
