#Desafio 043

from math import sqrt

peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / altura**2
print(imc)
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')