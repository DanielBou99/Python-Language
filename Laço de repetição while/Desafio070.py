#Desafio 070

print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)

barato =''
s = 0
k = 0
count = 0

while True:
    p = str(input('Nome do produto: '))
    v = float(input('preço: R$'))

    if count == 0:
        menor = v
        barato = p
        count +=1
    elif v < menor:
        menor = v
        barato = p


    s += v

    if v > 1000:
        k+=1

    while True:
        e = str(input('Quer continuar? [S/N]'))
        if e in 'SsNn':
            break
    if e in 'Nn':
        break

print('-'*30)
print(f'O total da compra foi {s}')
print(f'Temos {k} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor}')
