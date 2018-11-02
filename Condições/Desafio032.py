#Desafio 032

AnoUser = int(input('Ano: '))

if (AnoUser % 4 == 0 and AnoUser % 100 != 0) or (AnoUser % 400 == 0):
    print('O ano é Bissexto.')
else:
    print('O ano não é Bissexto.')
