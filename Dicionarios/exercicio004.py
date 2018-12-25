'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionario, incluindo o total de gols feitos
durante o campeonato.
'''

dic = {}
dic['nome'] = input('Nome: ')
partidas = int(input('Partidas: '))
lista = []
for i in range(0,partidas):
    partida = int(input(f'Partida {i+1}: '))
    lista.append(partida)
dic['gols'] = lista
dic['total'] = sum(lista)

print('-=' *30)

for k,v in dic.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' *30)

print(f'O jogador {dic["nome"]} jogou {partidas} partidas.')
for k,v in enumerate(dic['gols'],1):
    print(f'=> Na partida {k}, fez {v} gols.')
print(f'Foi um total de {dic["total"]} gols.')