'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionario, incluindo o total de gols feitos
durante o campeonato.
'''
totaljogadores = []
dic = dict()
while True:
    dic.clear()
    dic['nome'] = input('Nome: ').title()
    partidas = int(input('Partidas: '))
    lista = []
    for i in range(0,partidas):
        partida = int(input(f'Partida {i+1}: '))
        lista.append(partida)
    dic['gols'] = lista
    dic['total'] = sum(lista)
    totaljogadores.append(dic.copy())
    c = int(input('<0> para sair ou <1> para novo cadastro: '))
    print('-=' *30)
    if c == 0:
        break

print('cod',end=' ')
for i in dic.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for index,i in enumerate(totaljogadores):
    print(f'{index:>3}',end=' ')
    for v in i.values():
        print(f'{str(v):<15} ',end='')
    print()
print('-'*40)

while True:
    c = int(input('Quer mostrar os dados de qual jogador? <999> parar: '))
    if c == 999:
        print('<<Encerrado.>>')
        break
    elif c < 0 or c >= len(totaljogadores):
        print('<<Não há jogador com esse número.>>')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {totaljogadores[c]["nome"]}')
        for index,i in enumerate(totaljogadores[c]['gols']):
            print(f'No jogo {index+1} fez {i} gols.')
        print('-'*40)
