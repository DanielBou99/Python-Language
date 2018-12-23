# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
print('Modo aprendizado.')
soma = 0
lista = []
for numero in range(0,4):
    num = int(input(f'Digite a nota {numero+1}:'))
    soma += num
    lista.append(num)
print(f'Numeros informados: {lista} - Media: {soma/4:.2}')
print(f'Numeros informados: {lista} - Media: {sum(lista)/4:.2}')
