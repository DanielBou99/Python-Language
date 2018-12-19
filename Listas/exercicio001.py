'''
Escreva um programa que solicite vários números ao usuário,
sendo um de cada vez, possibilitando encerrar a entrada de dados
informando zero. Adicione os números informados em uma lista e,
ao final do programa, imprima a soma de todos os números,
a multiplicação de todos os números, o maior e o menor número informado.
'''

lista = []
while True:
    numero = int(input('Digite um numero (0 para sair)'))
    if numero == 0:
        break
    else:
        lista.append(numero)

if len(lista) > 0:
    soma = 0
    multiplicacao = 1
    maior, menor = lista[0], lista[0]

    for i,numero in enumerate(lista):
        soma += numero
        multiplicacao *= numero
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    if len(lista) == i+1:
        print('*' *30)
        print(f'Soma: {soma}')
        print(f'Multiplicação: {multiplicacao}')
        print(f'Maior: {maior}')
        print(f'Menor: {menor}')
else:
    print('Nenhum número informado.')
