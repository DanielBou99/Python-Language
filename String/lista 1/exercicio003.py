'''Crie um programa que solicite os seguintes dados ao usuário:
Informe o nome do produto:
Informe o preço do produto:
Informe a quantidade de produtos:
Ao final, usando composição de strings (%) imprima:
O produto NOME custa VALOR, você comprou QUANTIDADE e vai pagar TOTAL.
Lembre-se de formatar os floats com duas decimais.'''

produto = input('Produto: ')
preco = float(input('preço: '))
quantidade = int(input('Quantidade: '))
print('O produto %s custa R$ %.2f, você comprou %d e vai pagar R$ %.2f.'%(produto,preco,quantidade,quantidade*preco))
