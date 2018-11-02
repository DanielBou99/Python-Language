#Desafio 023

num = str(input('Numero:\n>>>'))

if (int(num) < 10):
    print('Unidade: {}'.format(int(num)))
elif (int(num) < 100):
    print('Dezena: {}'.format(int(num[0])))
    print('Unidade: {}'.format(int(num[1])))
elif (int(num) < 1000):
    print('Centena: {}'.format(int(num[0])))
    print('Dezena: {}'.format(int(num[1])))
    print('Unidade: {}'.format(int(num[2])))
elif (int(num) < 10000):
    print('Milhar: {}'.format(int(num[0])))
    print('Centeza: {}'.format(int(num[1])))
    print('Dezena: {}'.format(int(num[2])))
    print('Unidade: {}'.format(int(num[3])))
else:
    print('Numero incorreto.')