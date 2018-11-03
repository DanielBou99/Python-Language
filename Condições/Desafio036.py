#Desafio 036

ValorCasa = float(input('Valor da casa: '))
Salario = float(input('Salario: '))
Anos = int(input('Quantidade de anos: '))

Pmensal = ValorCasa / (Anos * 12)

if Pmensal > Salario*0.30:
    print('Emprestimo negado.')
    print('30% do salario: R$ {:.2f}\nValor do emprestimo: R$ {:.2f}'.format(Salario*0.30,Pmensal))
else:
    print('Emprestimo aprovado.')
    print('30% do salario: R$ {:.2f}\nValor do emprestimo: R$ {:.2f}'.format(Salario * 0.30, Pmensal))