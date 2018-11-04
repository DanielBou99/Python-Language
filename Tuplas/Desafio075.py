#Desafio 075

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor : '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor  : '))

tupla = (n1,n2,n3,n4)

k=0

print(f'Você digitou os valores {tupla}')

print(f'Você digitou {tupla.count(9)} vezes o valor 9.')

if 3 in tupla:
    print(f'O primeiro valor 3 está na {tupla.index(3)+1}ª posição.')
else:
    print('o valor 3 não foi digitado.')

print('Os valores pares digitados foram: ')

for c in tupla:
    if c % 2 == 0:
        print(f'{c} ',end='')