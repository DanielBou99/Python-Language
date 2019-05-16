# 2. Aplicando o Paradigma Funcional
# a. Usuário deve entrar com uma sequencia numérica de inteiros,
# e deve exibir na telas duas linhas, uma linha com os números ímpares,
# e outra linha com os pares

x = list(map(int,input().split()))
print(f'Pares:  {list(filter(lambda x: x%2==0,x))} ')
print(f'Impares: {list(filter(lambda x: x%2,x))} ')
