#Desafio 055

maior,menor = 0,0

for i in range(0,5):
    peso = float(input('{}º peso: '.format(i+1)))
    if i == 0:
        maior,menor = peso,peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('maior peso: {}\nmenor peso: {}'.format(maior,menor))

