'''Crie um programa que solicite uma palavra ao usuário e armazene
esta palavra em uma variável denominada 'palavra'.
Em seguida imprima o conteúdo da variável 20 vezes usando a multiplicação de strings.
Lembre-se de colocar um espaço para não imprimir as palavras "coladas".'''

palavra = input('Palavra: ')
palavra += ' '
print('{} '.format(palavra*20))
