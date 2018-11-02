#Desafio 026

frase = str(input('Frase\n>>>'))

frase = frase.strip().lower()

print('Letra A aparece {} vezes.'.format(frase.count('a')))

print('Primeira posição: {}'.format(frase.find('a')+1))

print('Ultima posição: {}'.format(frase.rfind('a')+1))