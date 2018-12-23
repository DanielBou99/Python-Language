# Faça um Programa que leia um vetor de 10 números reais e
# mostre-os na ordem inversa.

lista = []

for i in range(0,10):
    numero = int(input(f'Digite o numero {i+1}: '))
    lista.append(numero)
print(f'Números informados: {lista}')
lista.reverse()
print(f'Sequência invertida: {lista}')
