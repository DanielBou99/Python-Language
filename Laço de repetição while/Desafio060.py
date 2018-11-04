#Desafio 060

n = int(input('Número: '))
f = 1

while (n != 0):
    f *= n
    n -= 1

print('O fatorial é {}.'.format(f))