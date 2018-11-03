#Desafio 037

decimal = int(input('Numero decimal: '))

print('Escolha:\n1 para binário.\n2 para octal.\n3 para hexadecimal.')
escolha = int(input('>>>'))

if escolha == 1:
    print('Decimal {} para Binario {}'.format(decimal,bin(decimal)))
elif escolha == 2:
    print('Decimal {} para Octal {}'.format(decimal,oct(decimal)))
elif escolha == 3:
    print('Decimal {} para hexa {}'.format(decimal,hex(decimal)))
else:
    print('Escolha inválida.')
