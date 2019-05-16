# Aplicando o Paradigma Imperativo
# a. Usuário deve entrar com uma sequencia numérica de inteiros em uma linha,
# exiba na tela qual o maior, qual o menor, e calcule a média aritmética
# dos valores.

x = list(map(int,input().split()))

print(x)
print(max(x))
print(min(x))
print(f"Media aritmetica: {sum(x) / len(x)}")

