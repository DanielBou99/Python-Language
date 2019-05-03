
from calculariptu import *

imovel1 = Imovel(2,100)
imovel2 = Imovel(2,200.0)

casa1 = Casa(100.0,100.0,100.0,100.0)
casa2 = Casa(100.0,100.0,100.0,100.0)
casa3 = Casa(100.0,100.0,100.0,100.0)

imoveis = [imovel1,imovel2,casa1,casa2,casa3]

total = 0
for i in imoveis:
    i = i.calcularIPTU()
    total += i
    print(i)
print(f'total = {total}')