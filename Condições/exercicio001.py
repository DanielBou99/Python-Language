'''
Cálculo de média escolar
Faça um programa que solicite ao usuário o nome do aluno e quatro notas (em ponto
flutuante, float), calcule a média das notas e faça a validação da média conforme regra a
seguir: Se a média for menor que 5, o aluno está reprovado, se for maior ou igual a 5 ele
está de recuperação e se for maior ou igual a 7, ele está aprovado.
Ao final, imprima desta forma: “O aluno nome está resultado. Sua média foi media”, onde
nome é a variável que vai armazenar o nome digitado pelo usuário e resultado é a variável
que vai armazenar “aprovado”, “reprovado” ou “recuperação” e média é a variável que
vai armazenar a média calculada
'''
nome = input('Nome: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))
media = (n1+n2+n3+n4)/4
if media < 5:
    resultado = 'REPROVADO'
elif media >= 5:
    resultado = 'RECUPERAÇÃO'
elif media >=7:
    resultado = 'APROVADO'
print('O aluno {} está {}. Sua média foi {}'.format(nome,resultado,media))
