#Desafio 071

print('-'*30)
print('CAIXA ELETRÔNICO')
print('Notas disponíveis: [50/20/10/1]')
print('-'*30)


valor = int(input('Valor a ser sacado: '))

n50 = n20 = n10 = n1 = 0

n50 = valor // 50
valor -= n50 * 50

n20 = valor // 20
valor -= n20 * 20

n10 = valor // 10
valor -= n10 * 10

n1 = valor
valor -= valor

print(f"""
{int(n50)} notas de R$50
{int(n20)} notas de R$20
{int(n10)} notas de R$10
{int(n1)}  notas de R$1
""")

