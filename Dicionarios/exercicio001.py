'''
Um programa que leia nome e média de um aluno, guardando também a situação
em um dicionario. No final, mostre o conteudo na tela.
'''

dic = {}
dic['nome'] = input('Nome: ')
dic['nota'] = float(input('Nota: '))
dic['situacao'] = input('Situação: ')

for k,v in dic.items():
    print(f'{k} : {v}.')
