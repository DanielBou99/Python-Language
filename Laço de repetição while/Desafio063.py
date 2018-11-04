#Desafio 063
print('*'*30)
n = int(input('Quantidade de termos Fibonacci: '))
print('*'*30)

i = 0
f = 1
auxa = 1
auxs = 1

print('0 -> ',end='')

while i <= n:

    if i == 1:
        print('1 -> ',end='')
    elif i == 2:
        print('1 -> ',end='')
    elif i > 2:
        f = auxa + auxs
        auxa = auxs
        auxs = f

        print('{} -> '.format(f), end='')

    i+=1

print('FIM')
