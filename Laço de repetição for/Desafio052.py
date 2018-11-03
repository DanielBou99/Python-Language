#Desafio 042

n = int(input('Numero: '))
c = 0

for i in range(1,n+1):
    if n % i == 0:
        c += 1

print('É primo.' if c==2 else 'Não é primo.')
