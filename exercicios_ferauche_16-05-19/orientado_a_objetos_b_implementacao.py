'''
Implementacao
Paradigma Orientado a Objeto
b. Entre com uma sequencia de no mínimo 5 números reais, calcule a média
ponderada, utilizando 0.3 para os dois primeiros valores e para os dois
últimos valores, e a 0.1 para os valores intermediários, exiba o resultado. 
'''

from orientado_a_objetos_b_orientacao import *

while(True):
    x = list(map(float,input().split()))
    if (len(x) >= 5):
        break

aux = Pai(x)
aux.exibir()
