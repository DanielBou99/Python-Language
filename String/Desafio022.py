#Desafio 22

nome = str(input('Nome:>>'))

nome = nome.strip()

print('Todas as letras maiusculas: {}'.format(nome.upper()))

print('Todas as letras minusculas: {}'.format(nome.lower()))

print('Total de letras: {}'.format(len(nome.replace(' ',''))))

dividido = nome.split()
print(dividido[0])
print('Total de letras do primeiro nome: {}'.format(len(dividido[0])))
