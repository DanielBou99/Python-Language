'''
Escreva um programa que solicite várias palavras ao usuário,
sendo uma de cada vez, possibilitando encerrar a entrada de
dados informando zero. Adicione as palavras informadas
em uma lista. Após o usuário informar “0” (zero),
solicite a palavra que ele deseja contar. Desta forma,
o programa deverá contar as ocorrências daquela palavra.
Ao final imprima o resultado.
'''

lista = []
while True:
    palavra = input('Digite a palavra(0 para terminar): ')
    if palavra == '0':
        break
    lista.append(palavra.upper())
if len(lista) == 0:
    print('Nenhuma palavra informada')
else:
    lista.sort()
    palavra = input('Informe a palavra que deseja contar: ')
    print('*'*30)
    print(f'Palavras digitadas:\n{lista}')
    print(f'Temos {lista.count(palavra.upper())} ocorrências de {palavra}.')
