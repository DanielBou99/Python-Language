#Desafio 073

times = ('Palmeiras','Flamengo','Internacional',
         'São Paulo','Grêmio','Atlético','Santos',
         'Santos','Atlético-PR','Cruzeiro','Fluminense',
         'Corinthians','Vasco da Gama','Bahia','Ceará SC',
         'Botafogo','América-MG','Chapecoense','Sport Recife',
         'EC Vitória','Paraná')

print('Apenas os 5 primeiros colocados:')
print(times[:5])

print('-*'*30)

print('Os últimos 4 colocados na tabela: ')
print(times[-4:])

print('-*'*30)

print('Lista dos times em ordem alfabética:')
print(sorted(times))

print('-*'*30)

print('Posição da Chapecoense: {}'.format(times.index('Chapecoense')+1))