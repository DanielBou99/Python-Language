#Desafio 031

km = float(input('Km: '))

if km <= 200.0:
    print('Valor total: R$ {}.'.format(km*0.50))
else:
    print('Valor total: R$ {}.'.format(km*0.45))
