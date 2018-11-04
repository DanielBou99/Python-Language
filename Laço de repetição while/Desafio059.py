#Desafio 059

e = 10

while e != 0:

    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))

    print("""MENU:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    e = int(input('>>>'))

    if e == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif e == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif e == 3:
        print('{} > {}'.format(n1,n2) if n1>n2 else '{} > {}'.format(n2,n1))
    elif e == 4:
        print('DIGITE OS NOVOS NUMEROS.')
    elif e == 0:
        print('SAINDO DO PROGRAMA.')
    else:
        print('Opção inválida.')