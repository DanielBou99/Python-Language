'''
Paradigma Imperativo
b. Entre com uma sequencia de no mínimo 5 números reais, calcule a média
ponderada, utilizando 0.3 para os dois primeiros valores e para os dois
últimos valores, e a 0.1 para os valores intermediários, exiba o resultado. 
'''
resultado = 0

while(True):
    x = list(map(float,input().split()))
    if (len(x) >= 5):
        break

aux = 1

for i in range(0, len(x)):
    
    if i == 0 or i == 1:
        aux = x[i] * 0.3
    elif i == len(x)-1 or i == len(x)-2:
        aux = x[i] * 0.3
    else:
        aux = x[i] * 0.1

    resultado += aux
    print(resultado)





