'''
Paradigma Funcional
b. Entre com uma sequencia de números inteiros na mesma linha, exiba a soma
somente dos números pares da sequencia digitada.
'''

x = list(map(int,input().split()))
pares = list(filter(lambda x: x%2==0,x))

print(sum(pares))
