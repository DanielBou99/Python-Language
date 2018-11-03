#Desafio 045

from random import randint

print('Jokenpô')
print('1 - pedra.\n2 - papel.\n3 - tesoura.')
user = int(input('>>> '))
pc = randint(1,3)

if user == 1 and pc == 1:
    print('EMPATE: PEDRA!')
elif user == 2 and pc == 2:
    print('EMPATE: PAPEL!')
elif user == 3 and pc == 3:
    print('EMPATE: TESOURA!')
elif user == 1 and pc == 2:
    print('User: pedra.\nPC: papel.\nPC GANHOU!')
elif user == 1 and pc == 3:
    print('User: pedra.\nPC: tesoura.\nVOCÊ GANHOU!')
elif user == 2 and pc == 1:
    print('User: papel.\nPC: pedra.\nVOCÊ GANHOU!')
elif user == 2 and pc == 3:
    print('User: papel.\nPC: tesoura.\nPC GANHOU!')
elif user == 3 and pc == 1:
    print('User: tesoura.\nPC: pedra.\n PC GANHOU!')
elif user == 3 and pc == 2:
    print('User: tesoura.\nPC: papel.\nUSER GANHOU!')
else:
    print('Opção inválida.')
