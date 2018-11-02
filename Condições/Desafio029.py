#Desafio 030

km = int(input('Km/h: '))

if (km > 80):
    print('Você foi multado em R$ {},00.'.format((km-80)*7))
else:
    print('Parabéns! Você está dirigindo a {}Km/h.'.format(km))