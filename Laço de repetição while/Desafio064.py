#Desafio 064

n,s,k = int(input('Digite o número: ')),0,0

if n != 999:
    while n != 999:
        k +=1
        s+= n
        n = int(input('Digite mais um número:' ))
print('SOMA -> ', s, '\nQUANTIDADE -> ', k)
