#Desafio 025

nome = str(input('Nome:\n>>>'))

nome = nome.strip()

if 'SILVA' in nome.upper():
    print('O seu nome contem ''Silva''.')
else:
    print('não encontrado.')
