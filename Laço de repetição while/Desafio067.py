#Desafio 067

while True:
    n = int(input('Quer ver a tabuada de que valor?'))
    if n < 0:
        break
    print('-'*30)
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    print('-'*30)
