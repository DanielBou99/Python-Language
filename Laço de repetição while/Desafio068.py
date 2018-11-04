#Desafio 068

from random import randint

k = 0

print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*30)

while True:
    user = int(input('Digite um valor: '))
    pc = randint(1,10)
    e = str(input('Par ou Ímpar? [P/I]'))
    print('-'*30)

    r = 'DEU PAR' if (pc+user)%2==0 else 'DEU IMPAR'

    print(f'Você jogou {user} e o computador {pc}. Total de {pc+user} {r}')
    print('-'*30)

    if r == 'DEU PAR' and e == 'P':
        print('Você GANHOU!')
        k+=1
    elif r == 'DEU IMPAR' and user == 'I':
        print('Você GANHOU!')
        k+=1
    else:
        break

print(f'GAME OVER! Você venceu {k} vezes.')
