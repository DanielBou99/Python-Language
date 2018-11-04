#Desafio 077

palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')

for p in range(0,len(palavras)):

    print(f'Na palavra {palavras[p]} temos: ',end='')

    if 'a' in palavras[p].lower():
        print('A -> ',end='')
    if 'e' in palavras[p].lower():
        print('E -> ',end='')
    if 'i' in palavras[p].lower():
        print('I -> ',end='')
    if 'o' in palavras[p].lower():
        print('O -> ',end='')
    if 'u' in palavras[p].lower():
        print('U -> ',end='')

    print('FIM.')
