#Desafio 065

n = int(input('Digite o primeiro valor: '))
k = 1
c = 'c'
s = n
maior = menor = n

while c in 'cC':
    c = str(input('[C] continuar\n[S] sair'))
    if c in 'Cc':
        k += 1
        n = int(input('Digite outro valor: '))
        s += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

media = s / k
print('Media: {}\nMaior: {}\nMenor: {}'.format(media,maior,menor))
