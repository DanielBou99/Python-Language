'''
Crie um programa que solicite ao usuário que informe o valor de seu salário,
o valor do salário mínimo e sua idade. Compare se o valor do salário é maior
que dois salários mínimos E se a idade informada é maior que 18 usando
operadores lógicos e relacionais. Imprima no final: "O resultado foi X",
sendo que X será "True" ou "False".
'''
salario = float(input('Salario: '))
salario_minimo = float(input('Salario minimo: '))
idade = int(input('Idade: '))
print('O resultado foi {}'.format(salario > (2*salario_minimo) and idade > 18))
