#Desafio 035

a = float(input('Numero 1: '))
b = float(input('Numero 2: '))
c = float(input('Numero 3: '))

if (a < b+c and b < a+c and c < a+b):
    print('True: pode ser um triangulo.')
else:
    print('False: NÃO pode ser um triangulo.')