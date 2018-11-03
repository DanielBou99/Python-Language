#Desafio 044

preco = float(input('Preço do produto: '))

print('Menu:\n1- à vista dinheiro/cheque.\n2- à vista no cartão.')
print('3- em até 2x no cartão.\n4- 3x ou mais no cartão.')
e = int(input('Opção: '))

if e == 1:
    print('10% de desconto. Total a pagar = {}'.format(preco*0.90))
elif e == 2:
    print('5% de desconto. Total a pagar = {}'.format(preco*0.95))
elif e == 3:
    print('Preço normal. Total a pagar = {}'.format(preco))
elif e == 4:
    print('20% de juros. Total a pagar = {}'.format(preco*1.20))
else:
    print('Opção inválida.')
