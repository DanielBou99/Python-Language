#Desafio 027

nome = str(input('Nome:\n>>>'))

nome = nome.strip().title()

u = nome.count(' ')

nome = nome.split()

print('Primeiro = {}\nUltimo = {}\n '.format(nome[0], nome[u]))
