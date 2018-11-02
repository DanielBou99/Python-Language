#Desafio 024

cidade = str(input('Cidade:\n>>>'))

cidade = cidade.strip().split()

if cidade[0].upper() == 'SANTO':
    print('A cidade começa com a palavra Santos.')
else:
    print('A cidade NÃO começa com a palavra Santos.')

cidade = ' '.join(cidade)

print(cidade)
