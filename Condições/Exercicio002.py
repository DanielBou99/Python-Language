'''
Faça um programa que solicite ao usuário seu nome, sexo, peso em kg (float) e sua altura
em metros (float) e calcule o IMC. A validação deve seguir a seguinte regra:
**TABELA**
O resultado do programa deverá ser semelhante a este:
“Evaldo, com base no peso e altura informados, o IMC é imc e a condição é ‘condicao’.”
Onde imc é o cálculo obtido e condicao é uma das condições na tabela acima.
A equação para obter o imc é o peso em kg dividido pela altura em metros ao quadrado.
Desta forma:
'''
nome = input('Nome: ')
sexo = input('Sexo (F) Feminino ou (M) Masculino: ')
peso = float(input('Peso em kg: '))
altura = float(input('Altura em metros: '))
imc = peso / (altura*altura)
if sexo in 'Ff':
    if imc < 19.1:
        condicao = 'ABAIXO DO PESO'
    elif imc < 25.8:
        condicao = 'NO PESO NORMAL'
    elif imc < 27.3:
        condicao = 'MARGINALMENTE ACIMA DO PESO'
    elif imc < 32.3:
        condicao = 'ACIMA DO PESO IDEAL'
    else:
        condicao = 'OBESO'
else:
    if imc < 20.7:
        condicao = 'ABAIXO DO PESO'
    elif imc < 26.4:
        condicao = 'NO PESO NORMAL'
    elif imc < 27.8:
        condicao = 'MARGINALMENTE ACIMA DO PESO'
    elif imc < 31.1:
        condicao = 'ACIMA DO PESO IDEAL'
    else:
        condicao = 'OBESO'
print('{}, com base no peso e altura informados, o IMC é {:.2f} e a condição é {}.'.format(nome,imc,condicao))
    
