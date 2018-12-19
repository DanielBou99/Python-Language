''' Escreva um programa que solicite vários números ao usuário,
sendo um de cada vez, possibilitando encerrar a entrada de dados
informando zero. Armazene os números em uma lista, depois percorra
esta lista alimentando outras duas listas, uma com números pares
e outra com números ímpares. Imprima o resultado. '''

lista = []
pares, impares = [],[]

while True:
    numero = int(input('Informe um numero (0 para sair): '))
    if numero == 0:
        break
    lista += [numero]
if len(lista) == 0:
    print('Nenhum numero digitado.')
else:
    for numero in lista:
        if numero % 2 == 0:
            pares += [numero]
        else:
            impares += [numero]
    print('*'*30)
    print(f'''
Lista digitada: {lista}
Números impares: {impares}
Números pares: {pares}''')
