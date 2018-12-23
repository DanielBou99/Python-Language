'''
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''
vetor1 = []
vetor2 = []
vetor3 = []
vetor0 = []
teste = zip()

for i in range(1,31):
    if i < 11:
        vetor1.append(i)
    elif i < 21:
        vetor2.append(i)
    else:
        vetor3.append(i)
print(f'''Vetor 1: {vetor1}
Vetor 2: {vetor2}
Vetor 3: {vetor3}''')

for a,b,c in zip(vetor1,vetor2,vetor3):
    vetor0.append(a)
    vetor0.append(b)
    vetor0.append(c)

print(f'''Lista intercalada:
{vetor0}''')

