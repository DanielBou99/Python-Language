#Desafio 061

t1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
i = 0

print('{} -> '.format(t1),end='')
while i<=9:
    print('{} -> '.format(t1+razao),end='')
    t1 += razao
    i+=1
print('FIM')