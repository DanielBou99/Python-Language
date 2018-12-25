'''
Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados em um dicionario e todos os dicionario em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''

dic = {}
lista = []

while True:
    dic['nome'] = input('Nome: ').title()
    dic['sexo'] = input('Sexo: [M/F] ').upper()
    dic['idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    opcao = input('Quer continuar? [S/N] ')
    if opcao in 'Nn':
        break

print('-='*30)

totalpessoas = len(lista)
mediaidade = 0
for i in lista:
    mediaidade += i['idade']
mediaidade = mediaidade / totalpessoas
print(f'- O grupo tem {totalpessoas} pessoas.')
print(f'- A média de idade é de {mediaidade} anos.')
print('As mulheres cadastradas foram: ',end='')
for i in lista:
    if i['sexo'] in 'Ff':
        print(i['nome'],end='; ')
print('\n')
print('Pesssoas com idade acima da média:')
for i in lista:
    if i['idade'] > mediaidade:
        print(f'Nome: {i["nome"]}; Sexo: {i["sexo"]}; Idade: {i["idade"]}')
print('<<ENCERRADO>>')