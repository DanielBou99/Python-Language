'''
Programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionario se por acaso o CTPS for
diferente de ZERO, o dicionario receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.
'''

from datetime import datetime

dic = {}

anoatual = datetime.now()
anoatual = anoatual.year

dic['nome'] = input('Nome: ')
dic['idade'] = anoatual - int(input('Ano de nascimento: '))
dic['ctps'] = int(input('Carteira de trabalho (<0> não tem): '))
if dic['ctps'] != 0:
    dic['ctpsano'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salário: '))
    dic['aposentadoria'] = (35 - (anoatual - dic['ctpsano'])) + dic['idade']
else:
    dic['ctps'] = 'Não tem'

for k,v in dic.items():
    print(f'{k} tem o valor de {v}.')
