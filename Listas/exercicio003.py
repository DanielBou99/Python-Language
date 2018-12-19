'''
Escreva um programa que solicite vários números ao usuário,
sendo um de cada vez, possibilitando encerrar a entrada de
dados informando zero. Adicione os números em uma lista,
crie uma outra lista contendo os números sem repetição e
uma outra contendo os números que se repetem na primeira lista.
'''

lista = []
lista_repetidos = []
while True:
    numero = int(input('Informe um numero (0 para terminar): '))
    if numero == 0:
        break
    else:
        lista += [numero]
if len(lista) == 0:
    print('Nenhum numero informado')
else:
    print('*'*30)
    lista.sort()
    print(f'Numeros informados: {lista}.')
    for index,numero in enumerate(lista):
        contador = lista.count(numero)
        if contador > 1:
            for i in range(1,contador):
                lista.remove(numero)
                lista_repetidos += [numero]    

print(f'Lista sem repetição: {lista}.')
print(f'Numeros repetidos retirados: {lista_repetidos}.')

