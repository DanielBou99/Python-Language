#Desafio 062

t1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
q = int(input('Quantidade de termos: '))
i = 1

while q != 0:
    print('{} -> '.format(t1), end='')
    i = 1
    while i<=q:
        print('{} -> '.format(t1+razao),end='')
        t1 += razao 
        i+=1
    print('FIM')
    print('Quantos termos você quer mostrar a mais?')
    q = int(input(''))
print('FECHANDO O PROGRAMA.')