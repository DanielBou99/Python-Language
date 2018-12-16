while True:
    numero = int(input('Digite o numero entre 1 e 9: '))
    if numero >= 1 and numero <= 9:
        break
    else:
        print('Numero invalido.\n')
total = 0
for i in range(0,numero):
    total += int(input('Digite o {} numero: '.format(i))) * (i+1)
print('Total: {}'.format(total))
