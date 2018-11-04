#Desafio 057

sexo = str(input('Sexo (M) ou (F): ')).upper().strip()

while sexo not in 'MF':
    print('Você digitou incorretamente.')
    sexo = str(input('Sexo (M) ou (F): ')).upper().strip()
