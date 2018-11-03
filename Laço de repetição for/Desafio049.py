#Desafio 049

user = int(input('Número: '))
f = int(input('Final da tabuada: '))

for i in range(1, f+1):
    print('{} x {} = {}'.format(i,user,i*user))
