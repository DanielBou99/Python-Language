# import math
from math import sqrt,ceil,floor,factorial


n = int(input('Digite o numero:\n>>>'))
raiz = sqrt(n)
print('Raiz quadrada = {}'.format(raiz))
print('Arredondamento para cima = {}'.format(ceil(raiz)))
print('Arredondamento para baixo = {}'.format(floor(raiz)))
print('Fatorial = {}'.format(factorial(n)))