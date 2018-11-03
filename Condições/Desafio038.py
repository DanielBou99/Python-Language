#Desafio 038

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

if n1>n2:
    print('{} > {}'.format(n1,n2))
elif n2>n1:
    print('{} > {}'.format(n2,n1))
else:
    print('{} == {}'.format(n1,n2))
