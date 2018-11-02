#Desafio 034

salario = float(input('Salario: '))

if salario > 1250.00:
    print('{} com 10% de aumento: {:.2f}'.format(salario,salario*1.10))
else:
    print('{} com 15% de aumento: {:.2f}'.format(salario,salario*1.15))
