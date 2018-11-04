#Desafio 069

k = 0
tm = 0
tf = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    Idade = int(input('Idade: '))

    while True:
        Sexo = str(input('Sexo: [M/F] '))
        if Sexo in 'MmFf':
            break

    # CHECAGENS

    if Idade > 18:
        k += 1
    if Sexo in 'Mm':
        tm += 1
    if Sexo in 'Ff' and Idade < 20:
        tf += 1

    print('-'*30)

    while True:
        e = str(input('Quer continuar? [S/N] '))
        if e in 'SsNn':
            break

    if e in 'Nn':
        break

print(f'Total de pessoas com mais de 18 anos: {k}.')
print(f'Ao todo temos {tm} homens cadastrados.')
print(f'E temos {tf} mulheres com menos de 20 anos.')