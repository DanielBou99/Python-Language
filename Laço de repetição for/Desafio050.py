#Desafio 050

s = 0

for i in range(0,6):
    user = int(input('Numero: '))
    if user % 2 == 0:
        s += user
print('Soma = {}'.format(s))
