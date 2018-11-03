#Desafio 039

ano = int(input('Digite o ano de nascimento: '))

ano = 2018 - ano

if ano == 18:
    print('Esse é o seu ano de alistamento!')
elif ano < 18:
    print('Você ainda não tem 18 anos. Faltam {} anos.'.format(18-ano))
else:
    print('Você está atrasado {} anos para se alistar.'.format(ano-18))
