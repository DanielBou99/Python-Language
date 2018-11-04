#Desafio 074

from random import randint

sorteados = (randint(1,10),randint(1,10),randint(1,10),
             randint(1,10),randint(1,10))

print(f'Números sorteados foram: {sorted(sorteados)}')
print(f'Menor número: {min(sorteados)}')
print(f'Maior número: {max(sorteados)}')
