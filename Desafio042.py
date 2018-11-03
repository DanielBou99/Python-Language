#Desafio 042

a = float(input('Informe o lado A: '))
b = float(input('Informe o lado B: '))
c = float(input('Informe o lado C: '))

if a < b+c and b < a+c and c < a+b:
    if a == b == c:
        print('Equilátero.')
    elif a == b or a == c or c == b:
        print('Isósceles.')
    else:
        print('Escaleno.')