#Desafio 051

i = int(input('Primeiro termo: '))
c = int(input('Razão da PA: '))
f = c * 10 + i

for a in range(i, f, c):
    print('{} -> '.format(a),end='')
print('ACABOU.')
