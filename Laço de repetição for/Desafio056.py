#Desafio 056

midade = 0
maior = 0
fMenoresDe20Anos = 0
hmaisvelho = ''

for i in range(0,4):

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F) ou (M): ')).upper().strip()

    midade += idade

    if i == 0:
        maior = idade
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            hmaisvelho = nome

    if sexo == 'F' and idade < 20:
        fMenoresDe20Anos += 1

midade = midade / 4

print('Média do grupo: {}'.format(midade))
print('Homem mais velho: {}'.format(hmaisvelho))
print('Mulheres menores < 20 anos: {}'.format(fMenoresDe20Anos))