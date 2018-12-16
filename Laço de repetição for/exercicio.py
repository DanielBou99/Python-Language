while True:
    user = input('Informe um numero ou -sair- para finalizar: ')
    if user.lower() == 'sair':
        break
    elif int(user) % 2 == 0:
        print(f'{int(user)} é um número par.')
    else:
        print(f'{int(user)} é um número impar.')
