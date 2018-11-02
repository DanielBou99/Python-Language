# var = 'Daniel'
# print('Nome = {:*^20}!'.format(var))

n1 = int(input('First number = '))
n2 = int(input('Second number = '))

print('>Soma = {}, >Subtração = {}, >Multiplicação = {}\n'.format(n1+n2,n1-n2,n1*n2), end='>')
print('Divisão = {}, >Divisão Inteira = {}, >Potência = {} '.format(n1/n2,n1//n2,n1**n2))
